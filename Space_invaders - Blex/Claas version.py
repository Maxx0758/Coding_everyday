import pygame
from pygame import mixer
import random
import math

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
mixer.music.set_volume(0.07)
mixer.music.play(-1)

class Main():

    def __init__(self):
        self.width = width
        self.height = height
        self.bullet_state = bullet_state
        self.playerX = playerX
        self.playerY = playerY
        self.bulletX = bulletX
        self.bulletY = bulletY
        self.tomatoX = tomatoX
        self.tomatoY = tomatoY
        self.playerX_movement = playerX_movement
        self.bulletY_movement = bulletY_movement
        self.tomatoX_movement = tomatoX_movement
        self.bulletImg = bulletImg
        self.playerImg = playerImg
        self.tomatoImg = tomatoImg
        self.score_value = score_value
        self.screen = screen
        self.icon = icon
        self.background = background

    def player(self, x, y):
        screen.blit(self.playerImg, (x, y))

    def enemy_tomato(self, x, y, i):
        screen.blit(self.tomatoImg[i], (x, y))

    def fire_bullet(self, x, y):
        bullet_state = "fire"
        # The reason for adding pixels to x and y is so it
        # looks like it is gettings shot from the top midle of the player
        screen.blit(self.bulletImg, (x + 10, y + 10))

    def isCollision(self, tomatoX, tomatoY, bulletX, bulletY):
        distance = math.sqrt((math.pow(tomatoX-bulletX,2)) + (math.pow(tomatoY-bulletY,2)))
        if distance < 25:
            return True
        else:
            return False

    def show_score(self, x, y):
        score = font.render("Score: {}".format(self.score_value), True, (255, 0, 0))
        screen.blit(score, (x, y))

    def game_over(self):
        gameOver = font2.render("GAME OVER", True, (255, 0, 0))
        screen.blit(gameOver, (200, 250))

    # display() is my function there draw everything
    def display(self):
        self.screen.fill((0, 0, 0))
        # Background for the screen (R, G, B)
        self.screen.blit(self.background, (0, 0))
        self.show_score(textX, textY)
        self.player(playerX, playerY)
        time = int((pygame.time.get_ticks()/600)*0.6)
        gameOver = font.render("Time: {}".format(time), True, (255, 0, 0))
        screen.blit(gameOver, (650, 10))

        # Creating a lot of tomatos/enemies
        for i in range(num_of_tomatoes):
            self.tomatoImg.append(pygame.image.load('tomato.png'))
            self.tomatoX.append(random.randint(0, 800))
            self.tomatoY.append(random.randint(30, 130))
            self.tomatoX_movement.append(1.5)

        # Game Over
        if time >= 25 and score_value <= 10:
            for j in range(num_of_tomatoes):
                self.tomatoY[j] = 2000
            gameOver = font2.render("GAME OVER", True, (255, 0, 0))
            screen.blit(gameOver, (200, 280))
        
        # Level passed
        if self.score_value >= 10 and time <=25:
            for j in range(num_of_tomatoes):
                self.tomatoY[j] = 2000
            gameWin = font2.render("LEVEL PASSED", True, (255, 0, 0))
            screen.blit(gameWin, (160, 280))


    # This is the Game Loop.
    def main(self):

        done = False
        while not done:


            self.display()

            # events are things like clicking on your keyboard or using your mouse to click on things on the board.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Movement for player
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.playerX_movement += -2.5
                    if event.key == pygame.K_RIGHT:
                        self.playerX_movement += 2.5
                    # Bullet from player
                    if event.key == pygame.K_SPACE:
                        if bullet_state is "ready":
                            bullet_sound = mixer.Sound('laser.wav')
                            bullet_sound.play()
                            self.bulletX = self.playerX
                            self.fire_bullet(self.bulletX, self.bulletY)

                # Movement stop when lifting your finger from the key
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.playerX_movement = 0


            self.playerX += self.playerX_movement

            # Checking boundaries to stop player from moving off the screen
            if playerX <= 0:
                self.playerX = 0
            elif playerX >= 740:
                self.playerX = 740

            # Tomato movement
            for i in range(num_of_tomatoes):
                self.tomatoX[i] += self.tomatoX_movement[i]
                if tomatoX[i] <= 0:
                    self.tomatoX_movement[i] = 1.5
                elif tomatoX[i] >= 740:
                    self.tomatoX_movement[i] = -1.5

                # Collision
                collision = self.isCollision(self.tomatoX[i], self.tomatoY[i], self.bulletX, self.bulletY)
                if collision:
                    explosion_sound = mixer.Sound('explosion.wav')
                    explosion_sound.play()
                    self.bulletY = 480
                    self.bullet_state = "ready"
                    score_value += 1
                    self.tomatoX[i] = random.randint(0, 735)
                    self.tomatoY[i] = random.randint(30, 130)

                self.enemy_tomato(tomatoX[i], tomatoY[i], i)

            # Bullet Movement
            if bulletY <= 0:
                self.bulletY = 480
                self.bullet_state = "ready"

            if bullet_state is "fire":
                self.fire_bullet(self.bulletX, self.bulletY)
                self.bulletY -= self.bulletY_movement

            pygame.display.update()
    
    def game_start(self):
        self.main()


if __name__ == "__main__":
    playing = Main()
    playing.game_start()
