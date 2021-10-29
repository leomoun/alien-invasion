#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : rectangle_shoot.py
# @Time    : 2021/10/22 10:51
# @Author  : Leo
# @Software: PyCharm
import sys
from time import sleep
import pygame
from rectangle_settings import RectangleSettings
from game_stats import GameStats
from rectangle import Rectangle
from button import Button
from left_ship import LeftShip
from right_bullet import RightBullet
from easy_button import EasyButton
from normal_button import NormalButton
from hard_button import HardButton

class RectangleShoot:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = RectangleSettings()
        # 指定屏幕尺寸。
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))

        # 全屏模式。
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rectangle Shooting")

        # 创建一个用于存储游戏统计信息的实例。
        self.stats = GameStats(self)

        self.ship = LeftShip(self)
        self.bullets = pygame.sprite.Group()

        # 创建矩形。
        self.rectangles = pygame.sprite.Group()
        self._create_rectangle()

        # 创建Play按钮。
        self.play_button = Button(self, "Play")
        # 创建Easy按钮。
        self.easy_button = EasyButton(self, "Easy")
        # 创建Normal按钮。
        self.normal_button = NormalButton(self, "Normal")
        # 创建Hard按钮。
        self.hard_button = HardButton(self, "Hard")

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_rectangle()
                self._update_bullets()

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    self._choice_difficult_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """在玩家单击Play按钮时开始新游戏。"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()
            self._start_game()

    def _choice_difficult_button(self, mouse_pos):
        """在玩家单击easy, normal, hard按钮时选择难度。"""
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        normal_button_clicked = self.normal_button.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        if easy_button_clicked and not self.stats.game_active:
            # 按钮按下时变色
            self.easy_button.button_color = (200, 200, 200)
            self.screen.fill(self.easy_button.button_color, self.easy_button.rect)
            self.normal_button.button_color = (0, 0, 255)
            self.hard_button.button_color = (0, 0, 255)
            self.settings.easy = True
            self.settings.normal = False
            self.settings.hard = False
        elif normal_button_clicked and not self.stats.game_active:
            self.normal_button.button_color = (200, 200, 200)
            self.screen.fill(self.normal_button.button_color,
                             self.normal_button.rect)
            self.easy_button.button_color = (0, 0, 255)
            self.hard_button.button_color = (0, 0, 255)
            self.settings.easy = False
            self.settings.normal = True
            self.settings.hard = False
        elif hard_button_clicked and not self.stats.game_active:
            self.hard_button.button_color = (200, 200, 200)
            self.screen.fill(self.hard_button.button_color, self.hard_button.rect)
            self.normal_button.button_color = (0, 0, 255)
            self.easy_button.button_color = (0, 0, 255)
            self.settings.easy = False
            self.settings.normal = False
            self.settings.hard = True

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
        # 在游戏停止的情况下，按p键开始游戏。
        elif event.key ==pygame.K_p and not self.stats.game_active:
            self._start_game()
        # 在游戏停止的情况下，按e、n、h键调整游戏难度。
        elif event.key ==pygame.K_e and not self.stats.game_active:
            # 按钮按下时变色
            self.easy_button.button_color = (200, 200, 200)
            self.screen.fill(self.easy_button.button_color, self.easy_button.rect)
            self.normal_button.button_color = (0, 0, 255)
            self.hard_button.button_color = (0, 0, 255)
            self.settings.easy = True
            self.settings.normal = False
            self.settings.hard = False
        elif event.key == pygame.K_n and not self.stats.game_active:
            self.normal_button.button_color = (200, 200, 200)
            self.screen.fill(self.normal_button.button_color,
                             self.normal_button.rect)
            self.easy_button.button_color = (0, 0, 255)
            self.hard_button.button_color = (0, 0, 255)
            # pygame.display.flip()
            self.settings.easy = False
            self.settings.normal = True
            self.settings.hard = False
        elif event.key == pygame.K_h and not self.stats.game_active:
            self.hard_button.button_color = (200, 200, 200)
            self.screen.fill(self.hard_button.button_color, self.hard_button.rect)
            self.normal_button.button_color = (0, 0, 255)
            self.easy_button.button_color = (0, 0, 255)
            self.settings.easy = False
            self.settings.normal = False
            self.settings.hard = True

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

    def _start_game(self):
        """开始新游戏。"""
        # 重置游戏统计信息。
        self.stats.reset_stats()
        # 重置游戏设置
        self.settings.initialize_dynamic_settings()

        # 隐藏鼠标光标。
        pygame.mouse.set_visible(False)
        self.stats.game_active = True

        # 清空余下的子弹。
        self.bullets.empty()
        self.rectangles.empty()

        # 创建一个新的矩形，并将飞船放到屏幕左侧的中央。
        self.ship.midleft_ship()
        self._create_rectangle()

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
                self.stats.bullet_left -= 1
            elif pygame.sprite.groupcollide(self.bullets, self.rectangles,
                                          True, False):
                self.bullets.remove(bullet)
                self.settings.increase_speed()
        self._bullet_left()

    def _bullet_left(self):
        """判断是否还有剩余子弹，没有就重新开始游戏"""
        if self.stats.bullet_left == 0:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_rectangle_edges(self):
        """有矩形到达边缘时采取相应的措施。"""
        for rectangle in self.rectangles.sprites():
            if rectangle.check_edges():
                self.settings.rectangle_direction *= -1

    def _create_rectangle(self):
        # create a rectangle.
        rectangle = Rectangle(self)
        self.rectangles.add(rectangle)

    def _update_rectangle(self):
        """检查是否有矩形位于屏幕边缘，并更新外星人群中所有外星人的位置。"""
        self._check_rectangle_edges()
        self.rectangles.update()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for rectangle in self.rectangles.sprites():
            rectangle.draw_rectangle()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 如果游戏处于非活动状态，就绘制Play, Easy, Normal, Hard按钮。
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.normal_button.draw_button()
            self.hard_button.draw_button()

        # 让最近绘制的屏幕可见。
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = RectangleShoot()
    ai.run_game()