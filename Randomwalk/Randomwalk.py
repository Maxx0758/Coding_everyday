import pygame
import time
from random import randint

(width, height) = (1000,1000)
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Random walk game")
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 180)
radius = 30
running = True
fields = 10
#def drawObstacles():
    #piece = pygame.draw.circle(window, blue, SKRIVPOS, radius)

def drawBoard():
    #drawObstacles()
    color = [black, white]
    k = 0
    '''
    l = 0
    for k in range(0, fields):
                l += 1
                if l > 10:
                    l = 0
                #print(l)
                '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range (0, fields):
        if k == 0:
            farve = color[0]
            k = 1
        elif k == 1:
            farve = color[1]
            k = 0
        for j in range (0, fields):
            if k == 0:
                farve = color[0]
                k = 1
            elif k == 1:
                farve = color[1]
                k = 0
            '''
            if l == 1 or 3 or 5 or 7 or 9:
                color = (0, 0, 0)
                #print(color)             
            elif l == 0 or 2 or 4 or 6 or 8 or 10:
                color = (255, 255, 255)
                #print(color)
                '''
            
            pygame.draw.rect(window, farve, pygame.Rect(i * width / fields, j * height / fields, width / fields, height / fields))
            print(color)
            
def drawDirection():
    direction = randint(1,4)
'''    
def drawDice():
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
'''
while running:
    try:
        drawBoard()
        pygame.display.update()
    except Exception as e:
        print(e)
        print("There is an ERROR")
print("Tak for at du spillede")