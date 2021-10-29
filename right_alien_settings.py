#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : right_alien_settings.py
# @Time    : 2021/10/18 15:15
# @Author  : Leo
# @Software: PyCharm
class RightAlienSettings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置。"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = (255, 255, 255)

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3
        self.ship_killed = 0

        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60,60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction为1表示向下移，为-1表示向上移
        self.fleet_direction = 1
        self.alien_killed = 0