#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : rain.py
# @Time    : 2021/10/15 11:04
# @Author  : Leo
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite
from random import randint

class Rain(Sprite):
    """表示单个雨滴的类。"""

    def __init__(self, screen):
        """初始化雨滴并设置其起始位置。"""
        super().__init__()
        self.screen = screen

        # 加载雨滴图像并设置其rect属性
        self.image = pygame.image.load('images/rain_drop.bmp')

        # 随机缩小雨滴大小。
        # random_size = randint(10, 30)
        # self.image = pygame.transform.smoothscale(self.image, (random_size,
        #                                                        random_size))

        self.rect = self.image.get_rect()

        # 每颗雨滴最初都在屏幕左上角附近。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储雨滴的精确垂直位置。
        self.y = float(self.rect.y)

        # 雨滴设置
        self.drop_speed = 0.5
        # # fleet_direction为1表示向右移，为-1表示向左移
        # self.fleet_direction = 1

    # def check_edges(self):
    #     """如果一行雨滴消失在屏幕底端，就返回True"""
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.bottom >= screen_rect.bottom:
    #         return True

    def update(self):
        """雨滴下落。"""
        # drop_speed = 0.3
        self.y += self.drop_speed
        self.rect.y = self.y
        # self.rect.y += self.drop_speed

