import pygame
from random import randint
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (500, 500)
while(True):
    try:
        msg = input("Y what mate? ")
        if msg == "rect":
            side = randint(1, 6)
            radius = 40
            sizeRect  = (400, 400)
            posRect = ((width / 2) - (sizeRect[0] / 2), (height / 2) - (sizeRect[1] / 2))
            window = pygame.display.set_mode((width, height))
            window.fill(0)
            pygame.draw.rect(window, white, pygame.Rect(posRect, sizeRect))
            pygame.display.update()
            if(side == 1):
                posDot = (width / 2, height / 2)
                pygame.draw.circle(window, black, (int(posDot[0]), int(posDot[1])), radius)
                pygame.display.update()
            elif(side == 2):
                posDot1 = (125, 125)
                posDot2 = (width - 125, height - 125)
                pygame.draw.circle(window, black, (int(posDot1[0]), int(posDot1[1])), radius)
                pygame.draw.circle(window, black, (int(posDot2[0]), int(posDot2[1])), radius)
                pygame.display.update()
            elif(side == 3):
                posDot1 = (125, 125)
                posDot2 = (width - 125, height - 125)
                posDot3 = (width / 2, height / 2)
                pygame.draw.circle(window, black, (int(posDot1[0]), int(posDot1[1])), radius)
                pygame.draw.circle(window, black, (int(posDot2[0]), int(posDot2[1])), radius)
                pygame.draw.circle(window, black, (int(posDot3[0]), int(posDot3[1])), radius)
                pygame.display.update()
            elif(side == 4):
                posDot1 = (125, 125)
                posDot2 = (width - 125, height - 125)
                posDot3 = (125, height - 125)
                posDot4 = (width - 125, 125)
                pygame.draw.circle(window, black, (int(posDot1[0]), int(posDot1[1])), radius)
                pygame.draw.circle(window, black, (int(posDot2[0]), int(posDot2[1])), radius)
                pygame.draw.circle(window, black, (int(posDot3[0]), int(posDot3[1])), radius)
                pygame.draw.circle(window, black, (int(posDot4[0]), int(posDot4[1])), radius)
                pygame.display.update()
            elif(side == 5):
                posDot1 = (125, 125)
                posDot2 = (width - 125, height - 125)
                posDot3 = (125, height - 125)
                posDot4 = (width - 125, 125)
                posDot5 = (width / 2, height / 2)
                pygame.draw.circle(window, black, (int(posDot1[0]), int(posDot1[1])), radius)
                pygame.draw.circle(window, black, (int(posDot2[0]), int(posDot2[1])), radius)
                pygame.draw.circle(window, black, (int(posDot3[0]), int(posDot3[1])), radius)
                pygame.draw.circle(window, black, (int(posDot4[0]), int(posDot4[1])), radius)
                pygame.draw.circle(window, black, (int(posDot5[0]), int(posDot5[1])), radius)
                pygame.display.update()
            elif(side == 6):
                posDot1 = (125, 125)
                posDot2 = (width - 125, height - 125)
                posDot3 = (125, height - 125)
                posDot4 = (width - 125, 125)
                posDot5 = (width - 125, height / 2)
                posDot6 = (125, height / 2)
                pygame.draw.circle(window, black, (int(posDot1[0]), int(posDot1[1])), radius)
                pygame.draw.circle(window, black, (int(posDot2[0]), int(posDot2[1])), radius)
                pygame.draw.circle(window, black, (int(posDot3[0]), int(posDot3[1])), radius)
                pygame.draw.circle(window, black, (int(posDot4[0]), int(posDot4[1])), radius)
                pygame.draw.circle(window, black, (int(posDot5[0]), int(posDot5[1])), radius)
                pygame.draw.circle(window, black, (int(posDot6[0]), int(posDot6[1])), radius)
                pygame.display.update()
            #if(pygame.key.get_pressed):
                #side = randint(1, 6)
           
        elif msg == "quit":
            break
    except Exception as e:
        print(e)
        print("[ERROR] DIN MOR ER EN MAND")
print("Spurgt kurt")