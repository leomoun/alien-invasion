#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : rectangle_settings.py
# @Time    : 2021/10/22 10:57
# @Author  : Leo
# @Software: PyCharm
class RectangleSettings:
    """存储游戏rectangle_shoot中所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置。"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 默认游戏难度为normal
        self.easy = False
        self.normal = True
        self.hard = False

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 15
        self.bullet_height = 3
        # self.bullet_color = (60, 60,60)
        self.bullets_allowed = 3
        # 剩余子弹次数
        self.bullet_limit = 2

        # 矩形设置
        # 设置矩形的尺寸和其他属性。
        self.rectangle_width = 20
        self.rectangle_height = 100
        self.rectangle_color = (255, 0, 0)

        # rectangle_direction为1表示向下移，为-1表示向上移
        self.rectangle_direction = 1

        # 加快游戏节奏的速度。
        self.speedup_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """设置游戏不同等级难度"""
        if self.easy:
            self._easy_settings()
        elif self.normal:
            self._normal_settings()
        elif self.hard:
            self._hard_settings()

    def _easy_settings(self):
        """easy游戏难度的设置"""
        # 飞船设置
        self.ship_speed = 0.6

        # 子弹设置
        self.bullet_color = (0, 0, 255)
        self.bullet_speed = 1.5

        # 矩形设置
        self.rectangle_speed = 0.2
        print("easy")

    def _normal_settings(self):
        """normal游戏难度的设置"""
        # 飞船设置
        self.ship_speed = 0.8

        # 子弹设置
        self.bullet_color = (0, 0, 0)
        self.bullet_speed = 1.5

        # 矩形设置
        self.rectangle_speed = 0.3
        print("normal")

    def _hard_settings(self):
        """hard游戏难度的设置"""
        # 飞船设置
        self.ship_speed = 1

        # 子弹设置
        self.bullet_color = (255, 0, 0)
        self.bullet_speed = 1.5

        # 矩形设置
        self.rectangle_speed = 0.4
        print("hard")

    # def initialize_dynamic_settings(self):
    #     """初始化随游戏进行而变化的设置。"""
    #     # 飞船设置
    #     self.ship_speed = 1.5
    #     self.ship_killed = 0
    #
    #     # 子弹设置
    #     self.bullet_speed = 1.5
    #
    #     # 矩形设置
    #     self.rectangle_speed = 0.2
    #

    def increase_speed(self):
        """提高速度设置。"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.rectangle_speed *= self.speedup_scale