#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : rain_drop.py
# @Time    : 2021/10/15 11:04
# @Author  : Leo
# @Software: PyCharm
import sys
import pygame
from settings import Settings
from rain import Rain
from random import randint

def run_game():
    #初始化并创建资源。
    pygame.init()
    settings = Settings()
    # 指定屏幕尺寸。
    screen = pygame.display.set_mode((settings.screen_width,
                                           settings.screen_height))

    pygame.display.set_caption("Rain Drop")
    rains = pygame.sprite.Group()
    create_raindrops(screen, settings, rains)

    # 开始游戏的主循环
    while True:
        check_events()
        # rain_drop(rains)
        update_rains(rains, settings, screen)
        # update_rains(rains)
        update_screen(screen, settings, rains)

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

def available_spaces(screen, settings):
    rain = Rain(screen)
    rain_width, rain_height = rain.rect.size
    number_rain_x = settings.screen_width // (2 * rain_width)
    return number_rain_x

def create_raindrops(screen, settings, rains):
    rain = Rain(screen)
    number_rain_x = available_spaces(screen, settings)
    for rain_number in range(number_rain_x):
        create_a_raindrop(screen, rains, rain_number)

def create_a_raindrop(screen, rains, rain_number):
    rain = Rain(screen)
    rain_width, rain_height = rain.rect.size
    rain.rect.x = rain_width + 2 * rain_width * rain_number
    rains.add(rain)

def update_rains(rains, settings, screen):
    """更新雨滴的位置，并删除消失的雨滴。"""
    # 更新雨滴的位置。
    rains.update()
    for rain in rains.copy():
        if rain.rect.bottom >= settings.screen_height:
            rains.remove(rain)
    #         create_raindrops(screen, settings, rains)
    # print(len(rains))

    if rain.rect.bottom >= settings.screen_height:
        create_raindrops(screen, settings, rains)
    # print(len(rains))

def update_screen(screen, settings, rains):
    """更新屏幕上的图像，并切换到新屏幕。"""
    screen.fill(settings.bg_color)
    rains.draw(screen)

    # 让最近绘制的屏幕可见。
    pygame.display.flip()

run_game()