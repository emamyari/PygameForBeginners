import sys

import pygame

pygame.init()

width = 500
height = 710
fps = 60
floorx = 0
birdMove = 0
grav = 0.2
bg = pygame.transform.scale(pygame.image.load("assets/img/bg2.png"), (width, height))
floorimage = pygame.transform.scale(pygame.image.load("assets/img/floor.png"), (width, 225))
bird = pygame.transform.scale(pygame.image.load("assets/img/red_bird_mid_flap.png"), (50, 35))
birdDown=pygame.transform.scale(pygame.image.load("assets/img/red_bird_down_flap.png"), (50, 35))
birdUp=pygame.transform.scale(pygame.image.load("assets/img/red_bird_up_flap.png"), (50, 35))
birdRect = bird.get_rect(center=(50, 275 ))
win = pygame.display.set_mode([width, height])
pygame.display.set_caption("Flappy bird")
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birdMove = 0
                birdMove -= 5

    floorx -= 1
    birdMove += grav

    birdRect.centery += birdMove
    win.blit(bg, (0, 0))
    win.blit(bird, birdRect)
    if birdMove<0:
        win.blit(birdUp, birdRect)
    if birdMove>0:
        win.blit(birdDown, birdRect)
    win.blit(floorimage, (floorx, 550))
    win.blit(floorimage, (floorx + width, 550))

    if floorx <= -500:
        floorx = 0

    pygame.display.update()
    clock.tick(fps)

pygame.QUIT()
