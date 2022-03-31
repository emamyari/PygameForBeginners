import sys
import time

import pygame
import random

pygame.init()
birdEvent = pygame.USEREVENT
pygame.time.set_timer(birdEvent, 100)
pipeEvent = pygame.USEREVENT + 1
pygame.time.set_timer(pipeEvent, 1000)

fps = 90
width = 400
height = 800
floorX = 0
birdMove = 0
grav = 0.2
pipeList = []
game_status = True
score = 0
activeScore = True
highScore = 0

btn = pygame.transform.scale(pygame.image.load("assets/img/btn.png"),(120,50))
btnRect = btn.get_rect(center=(190, 415))

bg = pygame.transform.scale(pygame.image.load("assets/img/bg2.png"), (width, height))
floorImage = pygame.transform.scale(pygame.image.load('assets/img/floor.png'), (width, 200))
pipe = pygame.image.load("assets/img/pipe_green.png")

gameOverImage = pygame.image.load("assets/img/message.png")
gameOverImageRect = gameOverImage.get_rect(center=(190, 300))

winSound = pygame.mixer.Sound('assets/sound/smb_stomp.wav')
gameOverSound = pygame.mixer.Sound('assets/sound/smb_mariodie.wav')

bird_up = pygame.image.load("assets/img/red_bird_up_flap.png")
bird_mid = pygame.image.load("assets/img/red_bird_mid_flap.png")
bird_down = pygame.image.load("assets/img/red_bird_down_flap.png")

font = pygame.font.Font("assets/font/Flappy.TTF", 40)

bird_list = [bird_up, bird_mid, bird_down]
bird_index = 0
bird = bird_list[bird_index]

birdRect = bird.get_rect(center=(50, 300))
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


def generatePipeRect():
    rand_pos = random.randrange(350, 600)
    pipRect = pipe.get_rect(midtop=(400, rand_pos))
    pipRectUp = pipe.get_rect(midbottom=(400, rand_pos - 150))
    return pipRect, pipRectUp


def movePipe(pipes):
    for pipeRect in pipes:
        pipeRect.centerx -= 3
        if pipeRect.right < 0:
            pipes.remove(pipeRect)
    return pipes


def drawPipes(pipes):
    for piperect in pipes:
        if piperect.bottom > 450:
            win.blit(pipe, piperect)
        else:
            revImage = pygame.transform.rotate(pipe, 180)
            win.blit(revImage, piperect)


def checkCollision(pipes):
    # global activeScore
    for pipeRect in pipes:
        if birdRect.colliderect(pipeRect):
            # activeScore=True
            gameOverSound.play()
            time.sleep(3)
            return False
        if birdRect.top <= -20 or birdRect.bottom >= 600:
            # activeScore=True
            print(pipes)
            gameOverSound.play()
            time.sleep(3)
            return False
    return True


def birdAnime():
    newBird = bird_list[bird_index]
    newBirdRect = newBird.get_rect(center=(50, birdRect.centery))
    return newBird, newBirdRect


def displayScore(status):
    if (status == "active"):
        text = font.render(str(score), True, (255, 255, 255))
        textRect = text.get_rect(center=(185, 100))
        win.blit(text, textRect)
    if status == "game over":
        # score
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        textRect = text.get_rect(center=(185, 100))
        win.blit(text, textRect)
        # high score
        text2 = font.render("High Score: " + str(highScore), True, (255, 255, 255))
        textRect2 = text2.get_rect(center=(190, 500))
        win.blit(text2, textRect2)


def updateScore():
    global highScore
    global score, activeScore
    for pipeRect in pipeList:
        if 40 < pipeRect.centerx < 60 and activeScore:
            score += 1
            activeScore = False
        if pipeRect.centerx < 40:
            activeScore = True
    if score > highScore:
        highScore = score


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                winSound.play()
                birdMove = 0
                birdMove -= 5
            if event.key == pygame.K_t:
                game_status = True
                birdMove = 0
                score = 0
                pipeList.clear()
                birdRect.center = (50, 300)
        pos=pygame.mouse.get_pos()
        if btnRect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                print("left btn")

        if event.type == pipeEvent:
            pipeList.extend(generatePipeRect())
        if event.type == birdEvent:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, birdRect = birdAnime()

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
        updateScore()
        displayScore("active")
    else:
        displayScore("game over")
        win.blit(gameOverImage, gameOverImageRect)
        win.blit(btn,btnRect)
    if floorX <= -400:
        floorX = 0
    pygame.display.update()
    clock.tick(fps)
