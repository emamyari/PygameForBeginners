import sys

import pygame
import random

pygame.init()
fps = 90
width = 400
height = 800
floorX = 0
birdMove = 0
grav = 0.2
game_status = True
bg = pygame.transform.scale(pygame.image.load("assets/img/bg2.png"), (width, height))
floorImage = pygame.transform.scale(pygame.image.load('assets/img/floor.png'), (width, 200))
# bird = pygame.transform.scale2x(pygame.image.load("assets/img/red_bird_mid_flap.png"))
bird =  pygame.image.load("assets/img/red_bird_mid_flap.png")
pipe = pygame.image.load("assets/img/pipe_green.png")
birdRect = bird.get_rect(center=(50, 300))
pipeList = []
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pipeEvent = pygame.USEREVENT
pygame.time.set_timer(pipeEvent, 1000)


def generatePipeRect():
    rand_pos = random.randrange(350, 600)
    pipRect = pipe.get_rect(midtop=(400, rand_pos))
    pipRectUp = pipe.get_rect(midbottom=(400, rand_pos - 150))
    return pipRect, pipRectUp


def movePipe(pipes):
    for pipeRect in pipes:
        pipeRect.centerx -= 3
    return pipes


def drawPipes(pipes):
    for piperect in pipes:
        if piperect.bottom > 450:
            win.blit(pipe, piperect)
        else:
            revImage = pygame.transform.rotate(pipe, 180)
            win.blit(revImage, piperect)


def checkCollision(pipes):
    for pipeRect in pipes:
        if birdRect.colliderect(pipeRect):
            return False
        if birdRect.top <= -20 or birdRect.bottom >= 600:
            return False
    return True

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
            if event.key== pygame.K_t:
                game_status=True
                birdMove=0
                pipeList.clear()
                birdRect.center=(50,300)

        if event.type == pipeEvent:
            pipeList.extend(generatePipeRect())
    floorX -= 1
    birdMove += grav
    birdRect.centery += birdMove
    pipeList = movePipe(pipeList)

    win.blit(bg, (0, 0))
    if game_status:
        game_status = checkCollision(pipeList)
        drawPipes(pipeList)
        win.blit(bird, birdRect)
        win.blit(floorImage, (floorX, 650))
        win.blit(floorImage, (floorX + width, 650))

    if floorX <= -400:
        floorX = 0
    pygame.display.update()
    clock.tick(fps)
