import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 500))

# Background
background = pygame.image.load("L38-L37/background.png")

# Sound
mixer.music.load("L38-L37/background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("L38-L37/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('L38-L37/player.png')
playerX = 370
playerY = 380
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('L38-L37/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)#make the alien moving right automatically
    enemyY_change.append(40)#make the anien moving down automatically

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load("L38-L37/bullet.png")
bulletX = 0
bulletY = 380
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 32)

def show_score(x, y):
    score = font.render("score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_text.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    
    
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
    
        
# Game Loop
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("L38-L37/laser.wav")
                    bulletSound.play()
                    #get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0 


        playerX += playerX_change
        if playerX <= 0:
        
    elif playerX >= 736:
        

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 340:
            

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            
        elif enemyX[i] >= 736:
            

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    