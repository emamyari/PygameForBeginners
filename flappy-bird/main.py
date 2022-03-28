import sys

import pygame

pygame.init()
fps = 90
width = 400
height = 800
floorX=0
bg = pygame.transform.scale(pygame.image.load("assets/img/bg2.png"), (width, height))
floorImage = pygame.transform.scale(pygame.image.load('assets/img/floor.png'),(width, 200))

win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    floorX -=1

    win.blit(bg, (0, 0))
    win.blit(floorImage, (floorX, 650))
    win.blit(floorImage, (floorX+width, 650))
    if floorX<=-400:
        floorX=0

    pygame.display.update()
    clock.tick(fps)
