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
<<<<<<< HEAD
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




=======
floorimage = pygame.transform.scale(pygame.image.load("assets/img/floor.png"), (width, 225))
bird = pygame.transform.scale(pygame.image.load("assets/img/red_bird_mid_flap.png"), (50, 35))
birdDown=pygame.transform.scale(pygame.image.load("assets/img/red_bird_down_flap.png"), (50, 35))
birdUp=pygame.transform.scale(pygame.image.load("assets/img/red_bird_up_flap.png"), (50, 35))
birdRect = bird.get_rect(center=(50, 275 ))
win = pygame.display.set_mode([width, height])
pygame.display.set_caption("Flappy bird")
clock = pygame.time.Clock()
>>>>>>> 7636c7ba05ba4e61ee4b4660da52774588a137bd
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
<<<<<<< HEAD
        if event.type==pipeEvent:
            pipeList.append(generatePipeRect())

    floorX -= 1
    birdMove += grav
    birdRect.centery += birdMove
=======

    floorx -= 1
    birdMove += grav
>>>>>>> 7636c7ba05ba4e61ee4b4660da52774588a137bd

    birdRect.centery += birdMove
    win.blit(bg, (0, 0))
<<<<<<< HEAD

    pipeList=movePipe(pipeList)
    drawPipes(pipeList)

=======
>>>>>>> 7636c7ba05ba4e61ee4b4660da52774588a137bd
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
