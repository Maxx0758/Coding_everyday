from random import randint
import math
import pygame, sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode([800,600])

running = True

runde = True

White = (255, 255, 255)

Blue = (0, 0, 255)

pygame.font.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 30)
font2 = pygame.font.SysFont("comicsansms", 15)
text = font.render("What is the most effective transport", True, (255, 255, 255))
text2 = font2.render("Public transport", True, (255, 255, 255))
text3 = font2.render("Bike", True, (255, 255, 255))
text4 = font2.render("Car", True, (255, 255, 255))

while(running):
    try:
        mousePos = pygame.mouse.get_pos()
        print(mousePos)
        pygame.time.delay(100)

        if runde == True:

            window.fill((0,0,0))

            window.blit(text, (400 - text.get_width() // 2, 30 - text.get_height() // 2))
            window.blit(text2, (150 - text2.get_width() // 2, 75 - text2.get_height() // 2))
            window.blit(text3, (400 - text3.get_width() // 2, 75 - text3.get_height() // 2))
            window.blit(text4, (650 - text4.get_width() // 2, 75 - text4.get_height() // 2))
    
            pygame.display.flip()
            clock.tick(60)

            door1 = pygame.draw.rect(window, White, Rect((50, 100),(200, 400)))
            print(door1)

            door2 = pygame.draw.rect(window, White, Rect((300, 100),(200, 400)))
            print(door2)

            door3 = pygame.draw.rect(window, White, Rect((550, 100),(200, 400)))
            print(door2)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if door1.collidepoint(mousePos):
                        print("Forkert noob")
                        running = False
                        break
                    elif door2.collidepoint(mousePos):
                        print("Forkert noob")
                        running = False
                        break
                    elif door3.collidepoint(mousePos):
                        print("Når når du er pro")
                        andenRunde = True
                        runde = False
                        break

        
        if andenRunde == True:

            window.fill((0,0,0))

            door1 = pygame.draw.rect(window, Blue, Rect((50, 100),(200, 400)))
            print(door1)

            door2 = pygame.draw.rect(window, Blue, Rect((300, 100),(200, 400)))
            print(door2)

            door3 = pygame.draw.rect(window, Blue, Rect((550, 100),(200, 400)))
            print(door2)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if door1.collidepoint(mousePos):
                        print("Når når du er pro")
                        tredjeRunde = True
                        andenRunde = False
                        break
                    elif door2.collidepoint(mousePos):
                        print("Forkert noob")
                        running = False
                        break
                    elif door3.collidepoint(mousePos):
                        print("Forkert noob")
                        running = False
                        break

        if tredjeRunde == True:
            break

    except Exception as e:
        print(e)
        print("Unknown error")

print("\n Tak for spillet")
pygame.QUIT()

        