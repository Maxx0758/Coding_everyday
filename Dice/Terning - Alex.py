from random import randint
import math
import pygame
from pygame.locals import *

pygame.init()


while True:
    try:
        msg = input("\nHvad kan jeg hjælpe med?")
            
        if msg == "Terning":
           
            tal = randint(1, 6)
            
            radius = 50

            Black = (0, 0, 0)

            White = (255,255,255)

            if tal == 1:

                window = pygame.display.set_mode([640,600])

                window.fill((0,0,0))

                pygame.draw.rect(window, White, Rect((40, 40),(560, 520)))
                pos = (320, 300)
                pygame.draw.circle(window, Black, pos, radius)

                pygame.display.update()

                print(tal)

            elif tal == 2:

                window = pygame.display.set_mode([640,600])

                window.fill((0,0,0))
                pygame.draw.rect(window, White, Rect((40, 40),(560, 520)))
                pos1 = (150, 450)
                pos2 = (490, 150)
                pygame.draw.circle(window, Black, pos1, radius)
                pygame.draw.circle(window, Black, pos2, radius)
                

                pygame.display.update()

            elif tal == 3:

                window = pygame.display.set_mode([640,600])

                window.fill((0,0,0))
                pygame.draw.rect(window, White, Rect((40, 40),(560, 520)))
                pos1 = (130, 130)
                pos2 = (320, 300)
                pos3 = (510, 470)
                pygame.draw.circle(window, Black, pos1, radius)
                pygame.draw.circle(window, Black, pos2, radius)
                pygame.draw.circle(window, Black, pos3, radius)

                pygame.display.update()

            elif tal == 4:

                window = pygame.display.set_mode([640,600])

                window.fill((0,0,0))
                pygame.draw.rect(window, White, Rect((40, 40),(560, 520)))
                pos1 = (130, 130)
                pos2 = (510, 470)
                pos3 = (510, 130)
                pos4 = (130, 470)
                pygame.draw.circle(window, Black, pos1, radius)
                pygame.draw.circle(window, Black, pos2, radius)
                pygame.draw.circle(window, Black, pos3, radius)
                pygame.draw.circle(window, Black, pos4, radius)

                pygame.display.update()
            
            elif tal == 5:

                window = pygame.display.set_mode([640,600])

                window.fill((0,0,0))
                pygame.draw.rect(window, White, Rect((40, 40),(560, 520)))
                pos1 = (130, 130)
                pos2 = (510, 470)
                pos3 = (510, 130)
                pos4 = (130, 470)
                pos5 = (320, 300)
                pygame.draw.circle(window, Black, pos1, radius)
                pygame.draw.circle(window, Black, pos2, radius)
                pygame.draw.circle(window, Black, pos3, radius)
                pygame.draw.circle(window, Black, pos4, radius)
                pygame.draw.circle(window, Black, pos5, radius)

                pygame.display.update()

            elif tal == 6:

                window = pygame.display.set_mode([640,600])

                window.fill((0,0,0))
                pygame.draw.rect(window, White, Rect((40, 40),(560, 520)))
                pos1 = (130, 130)
                pos2 = (510, 470)
                pos3 = (510, 130)
                pos4 = (130, 470)
                pos5 = (130, 300)
                pos6 = (510, 300)
                pygame.draw.circle(window, Black, pos1, radius)
                pygame.draw.circle(window, Black, pos2, radius)
                pygame.draw.circle(window, Black, pos3, radius)
                pygame.draw.circle(window, Black, pos4, radius)
                pygame.draw.circle(window, Black, pos5, radius)
                pygame.draw.circle(window, Black, pos6, radius)

                pygame.display.update()

                
        
        elif msg == "quit":
            break

    except Exception as e:
        print(e)
        print("DER ER FEJL! Det er træls.")

print("\n Tak for nu")

            

