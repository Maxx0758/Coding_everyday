from random import randint
import math
import pygame
from pygame.locals import *

pygame.init()

running = True

runde = 1

White = (255, 255, 255)


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

        
        if runde == 2:
            break

        if runde == 3:
            break

    except Exception as e:
        print(e)
        print("Unknown error")

print("\n Tak for spillet")

        