#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : rectangle.py
# @Time    : 2021/10/22 10:54
# @Author  : Leo
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite

class Rectangle(Sprite):
    """矩形的类"""
    def __init__(self, ai_game):
        """create rectangle"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # 在(0,0)处创建一个矩形的rect对象，再使其居中。
        self.rect = pygame.Rect(0, 0, self.settings.rectangle_width,
                                self.settings.rectangle_height)
        self.rect.midright = self.screen_rect.midright

        # 存储矩形的精确垂直位置。
        self.y = float(self.rect.y)

    def check_edges(self):
        """如果矩形位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """向上或向下移动矩形。"""
        self.y += (self.settings.rectangle_speed *
                   self.settings.rectangle_direction)
        self.rect.y = self.y

    def draw_rectangle(self):
        """在屏幕上绘制矩形。"""
        pygame.draw.rect(self.screen, self.settings.rectangle_color, self.rect)