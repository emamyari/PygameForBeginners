from builtins import range
import time

import pygame
pygame.init()

width=900
hight=500
fps=60

pygame.mixer.init()
win=pygame.display.set_mode((width,hight))
sRed=pygame.image.load('aks/spaceship_red.png')
spRed = pygame.transform.rotate(pygame.transform.scale(sRed, (55, 40)), -90)
sYellow=pygame.image.load('aks/spaceship_yellow.png')
spYellow = pygame.transform.rotate(pygame.transform.scale(sYellow, (55, 40)), 90)

bg=pygame.image.load('aks/space.png')
bgp = pygame.transform.scale(bg, (width, hight))

bomb=pygame.mixer.Sound('aks/Grenade+1.mp3')
tir=pygame.mixer.Sound('aks/Gun+Silencer.mp3')

font = pygame.font.Font("aks/Flappy.TTF", 40)

red = pygame.Rect(700, 300, 55, 40)
yellow = pygame.Rect(100, 300, 55, 40)
clock = pygame.time.Clock()

gy=pygame.Rect(920, -20, 10, 5)
gr=pygame.Rect(-20, -20, 10, 5)

a=1
joonRed=2
joonYellow=2

while a>0:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = 0


    win.blit(bgp,(0,0))
    win.blit(spRed, (red.x, red.y))
    win.blit(spYellow, (yellow.x, yellow.y))
    pygame.draw.rect(win,(255,0,0),gy)
    pygame.draw.rect(win,(255,255,255),gr)

    text = font.render("HP: " + str(joonRed), True, (255, 255, 255))
    textRect = text.get_rect(center=(800, 50))
    win.blit(text, textRect)

    text = font.render("HP: " + str(joonYellow), True, (255, 255, 255))
    textRect = text.get_rect(center=(100, 50))
    win.blit(text, textRect)

    pygame.display.update()

    key_pressed=pygame.key.get_pressed()

    if (key_pressed[pygame.K_a] and red.x>450):
        red.x=red.x-5
    if (key_pressed[pygame.K_w] and red.y>0) :
        red.y=red.y-5
    if (key_pressed[pygame.K_d] and red.x<860):
        red.x=red.x+5
    if (key_pressed[pygame.K_s] and red.y<445):
        red.y = red.y +5

    if (key_pressed[pygame.K_LEFT] and yellow.x>0):
        yellow.x=yellow.x-5
    if (key_pressed[pygame.K_UP] and yellow.y>0):
        yellow.y=yellow.y-5
    if (key_pressed[pygame.K_RIGHT] and yellow.x<405):
        yellow.x=yellow.x+5
    if (key_pressed[pygame.K_DOWN] and yellow.y<445):
        yellow.y = yellow.y +5

    if (key_pressed[pygame.K_x] and gy.x>900):
        gy.x=yellow.x+40
        gy.y=yellow.y+25
        tir.play()

    gy.x+=7

    if (key_pressed[pygame.K_0] and gr.x<0):
        gr.x=red.x+40
        gr.y=red.y+25
        tir.play()

    gr.x-=7


    if gy.colliderect(red):
        bomb.play()
        gy.x=950
        joonRed=joonRed-1
        if joonRed==-1:
            a=0
            text = font.render("yellow win..." , True, (255, 255, 255))
            textRect = text.get_rect(center=(400, 250))
            win.blit(text, textRect)
            pygame.display.update()

            time.sleep(3)

    if gr.colliderect(yellow):
        bomb.play()
        gr.x=-20
        joonYellow-=1
        if joonYellow==-1:
            a=0
            text = font.render("red win..." , True, (255, 255, 255))
            textRect = text.get_rect(center=(400, 250))
            win.blit(text, textRect)
            pygame.display.update()

            time.sleep(3)