#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : right_alien.py
# @Time    : 2021/10/18 15:24
# @Author  : Leo
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite

class RightAlien(Sprite):
    """表示单个外星人的类。"""

    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置。"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近。
        self.rect.x = self.settings.screen_width - 2 * self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置。
        # self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """向上或向下移动外星人。"""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        # self.rect.y += (self.settings.alien_speed *
        #                self.settings.fleet_direction)
        # self.rect.x = self.x
        self.rect.y = self.y