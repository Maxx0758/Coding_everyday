from random import randint
import math
import pygame
from pygame.locals import *

pygame.init()

running = True

runde = 1

White = (255, 255, 255)

Blue = (0, 0, 255)


while(running):
    try:
        mousePos = pygame.mouse.get_pos()
        print(mousePos)

        if runde == 1:
            
            window = pygame.display.set_mode([800,600])

            window.fill((0,0,0))

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
                        andenRunde = 2
                        break
                    elif door2.collidepoint(mousePos):
                        print("Forkert noob")
                        andenRunde = 2
                        break
                    elif door3.collidepoint(mousePos):
                        print("Når når du er pro")
                        andenRunde = 2
                        break

        
        if andenRunde == 2:

            window = pygame.display.set_mode([800,600])

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
                        print("Forkert noob")
                        tredjeRunde == 3
                        break
                    elif door2.collidepoint(mousePos):
                        print("Forkert noob")
                        tredjeRunde == 3
                        break
                    elif door3.collidepoint(mousePos):
                        print("Når når du er pro")
                        tredjeRunde == 3
                        break

        if tredjeRunde == 3:
            break

    except Exception as e:
        print(e)
        print("Unknown error")

print("\n Tak for spillet")

        