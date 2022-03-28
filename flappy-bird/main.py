import sys

import pygame

pygame.init()
fps = 90
width = 400
height = 800

win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(fps)
