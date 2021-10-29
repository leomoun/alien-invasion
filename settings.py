#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : settings.py
# @Time    : 2021/9/17 17:19
# @Author  : Leo
# @Software: PyCharm
class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置。"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = (255, 255, 255)

        # 飞船设置
        self.ship_limit = 1

        # 子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60,60)
        self.bullets_allowed = 3
        # 剩余子弹次数
        self.bullet_limit = 1

        # 加快游戏节奏的速度。
        self.speedup_scale = 1.1
        # 外星人分数的提高速度。
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置。"""
        # 飞船设置
        self.ship_speed = 1.5
        self.ship_killed = 0

        # 子弹设置
        self.bullet_speed = 3.0

        # 外星人设置
        self.alien_speed = 0.5

        # 外星人设置
        self.fleet_drop_speed = 10

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        self.alien_killed = 0

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置和外星人分数。"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)