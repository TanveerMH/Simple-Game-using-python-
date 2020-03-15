'''
Assalamualikum,
This Game is Made by Hasan Tanveer Mahmood. Matric num: 1725413

Notes: If your compiler don't have Pygame Library Please install Pygame.

Procedure : 1. For move the fighter plane use keyboard arrow key
            2. use space key to kill the Enemy.
            3. If enemy touch ur Fighter plane the game will Quit.

'''

import math
import random

import pygame
from pygame import mixer

# Intialize the pygame library
pygame.init()

# Here I create the game screen
screen = pygame.display.set_mode((800, 600))

# This function is for background image
background = pygame.image.load('BG.png')

# This is the background sound
mixer.music.load("music.mp3")
mixer.music.play(-1)

# Welcoming message
pygame.display.set_caption("                                                              This Game Is Made By Hasan Tanveer Mahmood")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# fighter plane
fighterImg = pygame.image.load('PL1.png')
fighterX = 370
fighterY = 500
fighterXChange = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numOfEnymy = 7

for i in range(numOfEnymy):
    enemyImg.append(pygame.image.load('EN.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(40)

# Bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bulletPos = "ready"

# Score

scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def showScore(x, y):
    score = font.render("Score : " + str(scoreValue), True, (121, 255, 150))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (3, 200, 225))
    screen.blit(over_text, (200, 250))


def fighter(x, y):
    screen.blit(fighterImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bulletPos
    bulletPos = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # This condition is check whether user press right or left key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighterXChange = -4
            if event.key == pygame.K_RIGHT:
                fighterXChange = 4
            if event.key == pygame.K_SPACE:
                if bulletPos is "ready":
                    bulletSound = mixer.Sound("gun.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the fighter plane
                    bulletX = fighterX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fighterXChange = 0



    fighterX += fighterXChange
    if fighterX <= 0:
        fighterX = 0
    elif fighterX >= 736:
        fighterX = 736

    # Enemy Movement
    for i in range(numOfEnymy):

        # Game Over
        if enemyY[i] > 440:
            for j in range(numOfEnymy):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # Collision
        remove = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if remove:
            explosionSound = mixer.Sound("destroy.wav")
            explosionSound.play()
            bulletY = 480
            bulletPos = "ready"
            scoreValue += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bulletPos = "ready"

    if bulletPos is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    fighter(fighterX, fighterY)
    showScore(textX, testY)
    pygame.display.update()
