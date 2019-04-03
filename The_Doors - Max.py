import pygame
from random import randint

pygame.init()

(width, height) = (1500, 800)
running = True
doorWidth = 200
doorHeight = 400
brown = (102, 51, 0)
door1 = (100, 200)
door2 = ((width / 2) - (doorWidth / 2), 200)
door3 = (1200, 200)
Round = 1
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("The doors")
def startup():
    drawRound1()
def drawRound1():
    window.fill((255, 255, 255))
    pygame.draw.rect(window, brown, pygame.Rect((door1[0], door1[1]), (doorWidth, doorHeight)))
    pygame.draw.rect(window, brown, pygame.Rect((door2[0], door2[1]), (doorWidth, doorHeight)))
    pygame.draw.rect(window, brown, pygame.Rect((door3[0], door3[1]), (doorWidth, doorHeight)))
    pygame.display.update()
def drawRound2():
    window.fill((255, 255, 255))
    pygame.draw.rect(window, brown, pygame.Rect((door1[0], door1[1]), (doorWidth, doorHeight)))
    pygame.draw.rect(window, brown, pygame.Rect((door2[0], door2[1]), (doorWidth, doorHeight)))
    pygame.draw.rect(window, brown, pygame.Rect((door3[0], door3[1]), (doorWidth, doorHeight)))
    pygame.display.update()
def drawRound3():
    window.fill((255, 255, 255))
    pygame.draw.rect(window, brown, pygame.Rect((door1[0], door1[1]), (doorWidth, doorHeight)))
    pygame.draw.rect(window, brown, pygame.Rect((door2[0], door2[1]), (doorWidth, doorHeight)))
    pygame.draw.rect(window, brown, pygame.Rect((door3[0], door3[1]), (doorWidth, doorHeight)))
    pygame.display.update()
startup()

while(running):
    try:
        pygame.time.delay(100)
        mousePos = pygame.mouse.get_pos()
        print(mousePos)
        print(Round)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 100 <= mousePos[0] <= 300 and 200 <= mousePos[1] <= 600:
                    if Round == 1:
                        Round = 2
                        drawRound2()
                    elif Round == 2:
                        Round = 3
                        drawRound3()
                    elif Round == 3:
                        running = False
                elif 650 <= mousePos[0] <= 850 and 200 <= mousePos[1] <= 600:
                    if Round == 1:
                        Round = 2
                        drawRound2()
                    elif Round == 2:
                        Round = 3
                        drawRound3()
                    elif Round == 3:
                        running = False
                elif 1200 <= mousePos[0] <= 1400 and 200 <= mousePos[1] <= 600:
                    if Round == 1:
                        Round = 2
                        drawRound2()
                    elif Round == 2:
                        Round = 3
                        drawRound3()
                    elif Round == 3:
                        running = False
            break
    except Exception as e:
        print(e)
        print("[ERROR] Error in the program, fix it!")
print("Bye")