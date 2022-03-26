import pygame
import os

win = pygame.display.set_mode((900, 500))
pygame.display.set_caption("my game")
fps = 60
YSS = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YS=pygame.transform.rotate(pygame.transform.scale(YSS,(55,40)),90)

RSS = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RS=pygame.transform.rotate(pygame.transform.scale(RSS,(55,40)),270)

def draw():
    win.fill((255, 255, 255))
    win.blit(YS,(100,100))
    win.blit(RS,(700,100))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    pygame.quit()


main()
