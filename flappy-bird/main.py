import sys

import pygame

pygame.init()
fps = 90
width = 400
height = 800
floorX = 0
birdMove = 0
grav = 0.2
bg = pygame.transform.scale(pygame.image.load("assets/img/bg2.png"), (width, height))
floorImage = pygame.transform.scale(pygame.image.load('assets/img/floor.png'), (width, 200))
bird = pygame.transform.scale2x(pygame.image.load("assets/img/red_bird_mid_flap.png"))

birdRect = bird.get_rect(center=(50, 300))

win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                birdMove=0
                birdMove -=5

    print(birdMove)

    floorX -= 1
    birdMove+=grav
    birdRect.centery+=birdMove

    win.blit(bg, (0, 0))

    win.blit(bird, birdRect)
    win.blit(floorImage, (floorX, 650))
    win.blit(floorImage, (floorX + width, 650))
    if floorX <= -400:
        floorX = 0

    pygame.display.update()
    clock.tick(fps)
