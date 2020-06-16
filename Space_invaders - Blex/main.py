import pygame
from pygame import mixer
import random
import math
from random import randint

global k, not_picked

# Intialize the pygame
pygame.init()

# Create the screen with width and height
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Background
background = pygame.image.load("pølsevogn.jpg")
background = pygame.transform.scale(background, (800, 600))

# Title and Icon for the game screen
pygame.display.set_caption("Tomato Destroyer")
icon = pygame.image.load('tomato.png')
pygame.display.set_icon(icon)

# Player textures
# playerImg = pygame.image.load('space-invaders.png')
playerImg = pygame.image.load('dennis.png')
playerImg = pygame.transform.scale(playerImg, (120, 100))
playerX = width/2 - 30
playerY = 500

# Tomato textures
tomatoImg = []
tomatoX = []
tomatoY = []
tomato_movement = []
tomatoX_movement = []
num_of_tomatoes = 6
#tomatoImg = pygame.image.load('tomato.png')
#tomatoImg = pygame.transform.scale(tomatoImg, (60, 50))

# Bullet textures
# Ready - Bullet is not fired yet
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (60, 50))
bulletX = 0
bulletY = 500
bullet_state = "ready"

# Buff icons
saugageImg = pygame.image.load('buff_icon.png')
saugageImg = pygame.transform.scale(saugageImg, (60, 50))
saugageX = randint(0, 800)
saugageY = 500
saugage_state = "ready"
not_picked = False
k = 0

# Enemy bullet
bullet_tomatoX = 0
bullet_tomatoY = 500
tomato_bullet_state = "ready"

# Movement
playerX_movement = 0
bulletY_movement = 6

# Score
score_value = 0
textX = 10
textY = 10

# Textfonts
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 64)

# Music
mixer.music.load("bgmusic.wav")
# mixer.music.set_volume(0.8)
mixer.music.play(-1)

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy_tomato(x, y, i):
    screen.blit(tomatoImg[i], (x, y))

def sausage_buff(x, y):
    screen.blit(saugageImg, (x, y))

def sausage_collision(playerX, playerY, saugageX, saugageY):
    distance = math.sqrt((math.pow(playerX-saugageX, 2)) + (math.pow(playerY-saugageY, 2)))
    if distance < 25:
        return True
    else:
        return False

'''
def saugage_bullet(x, y):
    global bullet_state
    bullet_state = "buff_mode"
    # The reason for adding pixels to x and y is so it
    # looks like it is gettings shot from the top midle of the player
    screen.blit(bulletImg, (x + 10, y + 10))
'''

def fire_bullet(x, y):
    global bullet_state
    saugage_state = "buff_mode"
    bullet_state = "fire"
    # The reason for adding pixels to x and y is so it
    # looks like it is gettings shot from the top midle of the player
    screen.blit(bulletImg, (x + 10, y + 10))

def isCollision(tomatoX, tomatoY, bulletX, bulletY):
    distance = math.sqrt((math.pow(tomatoX-bulletX,2)) + (math.pow(tomatoY-bulletY,2)))
    if distance < 35:
        return True
    else:
        return False


# The two functions under are for enemy bullets, but this task is on pause because of failure.
'''
def fire_enemy_bullet(x, y):
    global tomato_bullet_state
    tomato_bullet_state = "fire"
    screen.blit(tomatoImg, (x - 10, y - 10))

def isDead(playerX, playerY, bullet_tomatoX, bullet_tomatoY):
    distance = math.sqrt((math.pow(playerX-bullet_tomatoX, 2)) +
                         (math.pow(playerY-bullet_tomatoY, 2)))
    if distance < 25:
        return True
    else:
        return False
'''

def show_score(x, y):
    score = font.render("Score: {}".format(score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))

def game_over():
    gameOver = font2.render("GAME OVER", True, (255, 0, 0))
    screen.blit(gameOver, (200, 250))

# display() is my function there draw everything
def display():
    screen.fill((0, 0, 0))
    # Background for the screen (R, G, B)
    screen.blit(background, (0, 0))
    show_score(textX, textY)
    player(playerX, playerY)
    time = int((pygame.time.get_ticks()/600)*0.6)
    gameOver = font.render("Time: {}".format(time), True, (255, 0, 0))
    screen.blit(gameOver, (650, 10))

    # Creating a lot of tomatos/enemies
    for i in range(num_of_tomatoes):
        tomatoImg.append(pygame.image.load('tomato.png'))
        tomatoX.append(random.randint(0, 800))
        tomatoY.append(random.randint(30, 130))
        tomatoX_movement.append(2.5)

    # Game Over
    if time >= 25 and score_value < 10:
        for j in range(num_of_tomatoes):
            tomatoY[j] = 2000
        gameOver = font2.render("GAME OVER", True, (255, 0, 0))
        screen.blit(gameOver, (200, 280))
    
    # Level passed
    if score_value >= 10 and time <=25:
        for j in range(num_of_tomatoes):
            tomatoY[j] = 2000
        gameWin = font2.render("LEVEL PASSED", True, (255, 0, 0))
        screen.blit(gameWin, (160, 280))
        
    if score_value >= 3:
        if not_picked == False:
            sausage_buff(saugageX, saugageY)
        else:
            pass


# This is the Game Loop.
running = True
while running:

    display()

    # events are things like clicking on your keyboard or using your mouse to click on things on the board.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement for player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_movement += -4.5
            if event.key == pygame.K_RIGHT:
                playerX_movement += 4.5
            # Bullet from player
            if event.key == pygame.K_SPACE:
                if k == 1:
                    saugage_state = "buff_mode"
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    fire_bullet(bulletX - 15, bulletY)
                    fire_bullet(bulletX + 15, bulletY)
                elif k == 0:
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        # Movement stop when lifting your finger from the key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_movement = 0


    playerX += playerX_movement

    # Checking boundaries to stop player from moving off the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 740:
        playerX = 740

    # Tomato movement
    for i in range(num_of_tomatoes):
        tomatoX[i] += tomatoX_movement[i]
        if tomatoX[i] <= 0:
            tomatoX_movement[i] = 1.5
        elif tomatoX[i] >= 740:
            tomatoX_movement[i] = -1.5

        # Collision
        collision = isCollision(tomatoX[i], tomatoY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            saugage_state = "ready"
            bullet_state = "ready"
            score_value += 1
            tomatoX[i] = random.randint(0, 735)
            tomatoY[i] = random.randint(30, 130)

        enemy_tomato(tomatoX[i], tomatoY[i], i)

        s_collision = sausage_collision(playerX, playerY, saugageX, saugageY)
        if s_collision and score_value >= 3:
            saugage_state = "buff_mode"
            k = 1
            not_picked = True
            # print("oof")

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        saugage_state = "ready"

    if saugage_state is "buff_mode" and bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        fire_bullet(bulletX - 15, bulletY)
        fire_bullet(bulletX + 15, bulletY)
        bulletY -= bulletY_movement

    elif bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_movement

    pygame.display.update()



















''