#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : star.py.py
# @Time    : 2021/10/14 15:29
# @Author  : Leo
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """表示单个星星的类。"""

    def __init__(self, screen):
        """初始化星星并设置其起始位置。"""
        super().__init__()
        self.screen = screen

        # 加载星星图像并设置其rect属性
        self.image = pygame.image.load('images/star.bmp')

        # 随机缩小星星大小。
        random_size = randint(10, 30)
        self.image = pygame.transform.smoothscale(self.image, (random_size,
                                                               random_size))

        self.rect = self.image.get_rect()

        # 每颗星星最初都在屏幕左上角附近。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储星星的精确水平位置。
        self.x = float(self.rect.x)
