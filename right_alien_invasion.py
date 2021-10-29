#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : right_alien_invasion.py
# @Time    : 2021/10/18 15:08
# @Author  : Leo
# @Software: PyCharm
import sys
from time import sleep
import pygame
from right_alien_settings import RightAlienSettings
from game_stats import GameStats
from left_ship import LeftShip
from right_bullet import RightBullet
from right_alien import RightAlien

class RightAlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = RightAlienSettings()
        # 指定屏幕尺寸。
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))

        # 全屏模式。
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # 创建一个用于存储游戏统计信息的实例。
        self.stats = GameStats(self)

        self.ship = LeftShip(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
            # 响应键盘和鼠标事件。
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键。"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开。"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中。"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = RightBullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置，并删除消失的子弹。"""
        # 更新子弹的位置。
        self.bullets.update()

        # 删除消失的子弹。
        for bullet in self.bullets.copy():
            # if bullet.rect.bottom <= 0:
            if bullet.rect.left > self.settings.screen_width:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        self._check_bullet_alien_collisons()

    def _check_bullet_alien_collisons(self):
        """响应子弹和外星人碰撞。"""
        # 删除发生碰撞的子弹和外星人。
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)

        if collisions:
            self.settings.alien_killed += 1
            print(f"alien_killed: {self.settings.alien_killed}")

        if not self.aliens:
            # 删除现有的子弹并新建一群外星人
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """创建外星人群。"""
        # 创建一个外星人，并计算一行可容纳多少个外星人。
        # 外星人的间距为外星人宽度。
        alien = RightAlien(self)

        alien_width, alien_height = alien.rect.size
        ship_width = self.ship.rect.width

        # 计算屏幕可容纳多少列外星人。
        available_space_x = (self.settings.screen_width - (4 * alien_width)
                             - ship_width)
        number_columns = available_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少行外星人。
        available_space_y = self.settings.screen_height - alien_height
        number_rows = available_space_y // int(1.5 * alien_height)

        # 创建外星人群。
        for column_number in range(number_columns):
            for row_number in range(number_rows):
                self._create_alien(column_number, row_number)

    def _create_alien(self, column_number, row_number):
        # 创建一个外星人，并将其放在当前列。
        alien = RightAlien(self)
        alien_width, alien_height = alien.rect.size
        # alien.x = (self.settings.screen_width - 2* alien_width - 2 *
        #            alien_width * column_number)
        # alien.rect.x = alien.x
        alien.rect.x = (self.settings.screen_width - 2 * alien_width - 2 *
                   alien_width * column_number)
        alien.y = alien_height + 1.5 * alien_height * row_number
        alien.rect.y = alien.y
        # alien.rect.y = alien_height + 1.5 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施。"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                # print("1")
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向。"""
        for alien in self.aliens.sprites():
            # alien.rect.x = alien.rect.x - self.settings.fleet_drop_speed
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_killed_account(self):
        """摧毁的飞船数。"""
        self.settings.ship_killed += 1
        print(f"ship_killed: {self.settings.ship_killed}")

        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.midleft_ship()
            sleep(1)
        else:
            self.stats.game_active = False

    def _update_aliens(self):
        """检查是否有外星人位于屏幕边缘，并更新外星人群中所有外星人的位置。"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检查是否有外星人撞到飞船。
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_killed_account()

        # """检查是否有外星人到达了屏幕底端。"""
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                self._ship_killed_account()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # 让最近绘制的屏幕可见。
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = RightAlienInvasion()
    ai.run_game()