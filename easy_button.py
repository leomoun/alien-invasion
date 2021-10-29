#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : easy_button.py
# @Time    : 2021/10/27 17:37
# @Author  : Leo
# @Software: PyCharm
import pygame.font

class EasyButton:

    def __init__(self, ai_game, msg):
        """初始化按钮的属性。"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸和其他属性。
        self.width, self.height = 150, 50
        self.button_color = (0, 0, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.button_color_down = (200, 200, 200)

        # 创建按钮的rect对象，并使其居中。
        self.rect = pygame.Rect(525, 435, self.width, self.height)

        # 按钮的标签只需创建一次。
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中。"""
        # self.msg_image = (self.font.render(msg, True, self.text_color,
        #                                    self.button_color))
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本。
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_button_down(self):
        self.button_color_down = (200, 200, 200)
        self.screen.fill(self.button_color_down, self.rect)
        # self.screen.blit(self.msg_image, self.msg_image_rect)
