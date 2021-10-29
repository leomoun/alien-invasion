#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : game_stats.py
# @Time    : 2021/10/21 10:10
# @Author  : Leo
# @Software: PyCharm
class GameStats:
    """跟踪游戏的统计信息。"""

    def __init__(self, ai_game):
        """初始化统计信息。"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 让游戏一开始处于非活动状态。
        self.game_active = False

        # 任何情况下都不应重置最高得分。
        # self.high_score = 0
        self.read_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息。"""
        self.ships_left = self.settings.ship_limit
        self.bullet_left = self.settings.bullet_limit
        self.score = 0
        self.level = 1

        # # 重置未击中次数为0.
        # self.settings.fail_times = 0

    def save_high_score(self):
        """将最高分保存在high_score文件中"""
        high_score_str = str(self.high_score)
        filename = 'high_score.txt'
        with open(filename, 'w') as file_object:
            file_object.write(high_score_str)

    def read_high_score(self):
        """
        读取high_score文件中保存的最高得分
        如果没有记录，则最高分为0
        """
        filename = 'high_score.txt'
        try:
            with open(filename) as file_object:
                contents = file_object.read()
            self.high_score = int(contents)
        except FileNotFoundError:
            self.high_score = 0