import pygame
import os
width=900
height=500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("my game")
fps = 60
pow=5
gol=10

YSS = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YS = pygame.transform.rotate(pygame.transform.scale(YSS, (55, 40)), 90)

RSS = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RS = pygame.transform.rotate(pygame.transform.scale(RSS, (55, 40)), 270)


def draw(red,yellow,gy):
    win.fill((255, 255, 255))
    win.blit(RS, (red.x, red.y))
    win.blit(YS, (yellow.x, yellow.y))
    pygame.draw.rect(win,(255,0,0),gy)
    pygame.display.update()

def yellow_move(key_pressed,yellow):
    if (key_pressed[pygame.K_a] and yellow.x>0):
        yellow.x -= pow
    if (key_pressed[pygame.K_d] and yellow.x+yellow.width<width//2):
        yellow.x += pow
    if (key_pressed[pygame.K_w]  and yellow.y>0 ):
        yellow.y -= pow
    if (key_pressed[pygame.K_s] and yellow.y+yellow.height<height-20):
        yellow.y += pow

def red_move(key_pressed,red):
    if (key_pressed[pygame.K_LEFT] and red.x>width//2 ):
        red.x -= pow
    if (key_pressed[pygame.K_RIGHT] and red.x+red.width<width):
        red.x += pow
    if (key_pressed[pygame.K_UP] and red.y>0  ):
        red.y -= pow
    if (key_pressed[pygame.K_DOWN]  and red.y+red.height<height-20):
        red.y += pow

def g_move(gy,gr,red,yellow):
    gy.x+=10
    if red.colliderect(gy):
        print("yeeeeees")

def main():
    red = pygame.Rect(700, 300, 55, 40)
    yellow = pygame.Rect(100, 300, 55, 40)

    clock = pygame.time.Clock()
    run = True
    gr=pygame.Rect(1,1,1,1)
    gy=pygame.Rect(1,1,1,1)
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gy=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2,5,5)

                if event.key == pygame.K_0:
                    gr=pygame.Rect(red.x+red.width,red.y+red.height//2,5,5)


        key_pressed=pygame.key.get_pressed()
        yellow_move(key_pressed,yellow)
        red_move(key_pressed,red)
        g_move(gy,gr,red,yellow)
        draw(red,yellow,gy)
    pygame.quit()


main()
