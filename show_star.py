#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : show_star.py
# @Time    : 2021/10/14 15:31
# @Author  : Leo
# @Software: PyCharm
import sys
import pygame
from settings import Settings
from star import Star
from random import randint

def run_game():
    #初始化并创建资源。
    pygame.init()
    settings = Settings()
    # 指定屏幕尺寸。
    screen = pygame.display.set_mode((settings.screen_width,
                                           settings.screen_height))

    pygame.display.set_caption("Show Star")
    stars = pygame.sprite.Group()
    create_star(screen, settings, stars)

    """开始游戏的主循环"""
    while True:
        check_events()
        update_screen(screen, settings, stars)

def check_events():
        # 响应键盘和鼠标事件。
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event)

def check_keydown_events(event):
    """响应按键。"""
    if event.key == pygame.K_ESCAPE:
        sys.exit()

def create_star(screen, settings, stars):
    """创建星星群。"""
    # 创建一颗星星，并计算一行可容纳多少颗星星。
    # 星星的间距为星星宽度。
    star = Star(screen)
    star_width, star_height = star.rect.size
    number_star_x = settings.screen_width // (2 * star_width)

    # 计算屏幕可容纳多少行星星。
    number_rows = (settings.screen_height // (randint(5, 10) *
                                                   star_height))

    # 创建star群。
    for row_number in range(number_rows):
        for star_number in range(number_star_x):
            star = Star(screen)
            star.x = randint(0, settings.screen_width)
            star.rect.x = star.x
            star.rect.y = randint(0, settings.screen_height)
            stars.add(star)

def update_screen(screen, settings, stars):
    """更新屏幕上的图像，并切换到新屏幕。"""
    screen.fill(settings.bg_color)
    stars.draw(screen)

    # 让最近绘制的屏幕可见。
    pygame.display.flip()

run_game()
