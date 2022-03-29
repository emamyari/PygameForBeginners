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
pipe = pygame.image.load("assets/img/pipe_green.png")
birdRect = bird.get_rect(center=(50, 300))
pipeList=[]
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pipeEvent = pygame.USEREVENT
pygame.time.set_timer(pipeEvent, 1000)

def generatePipeRect():
    pipRect=pipe.get_rect(midtop=(300,500))
    return pipRect

def movePipe(pipes):
    for pipeRect in pipes:
        pipeRect.centerx -=3
    return pipes

def drawPipes(pipes):
    for piperect in pipes:
        win.blit(pipe,piperect)




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
        if event.type==pipeEvent:
            pipeList.append(generatePipeRect())

    floorX -= 1
    birdMove += grav
    birdRect.centery += birdMove

    win.blit(bg, (0, 0))

    pipeList=movePipe(pipeList)
    drawPipes(pipeList)

    win.blit(bird, birdRect)
    win.blit(floorImage, (floorX, 650))
    win.blit(floorImage, (floorX + width, 650))
    if floorX <= -400:
        floorX = 0

    pygame.display.update()
    clock.tick(fps)
