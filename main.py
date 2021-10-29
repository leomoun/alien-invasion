# 12-1:
import sys
import pygame

def create_screen():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue")

    while True:
        # 设置背景色。
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

        pygame.display.flip()

create_screen()