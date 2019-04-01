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
runde = 1
while(running):
    try:
        window = pygame.display.set_mode((width,height))
        mousePos = pygame.mouse.get_pos()
        print(mousePos)
        if runde == 1:
            window.fill((255, 255, 255))
            pygame.draw.rect(window, brown, pygame.Rect((door1[0], door1[1]), (doorWidth, doorHeight)))
            pygame.draw.rect(window, brown, pygame.Rect((door2[0], door2[1]), (doorWidth, doorHeight)))
            pygame.draw.rect(window, brown, pygame.Rect((door3[0], door3[1]), (doorWidth, doorHeight)))
            pygame.display.update()
        elif runde == 2:
            window.fill((255, 255, 255))
            pygame.draw.rect(window, brown, pygame.Rect((door1[0], door1[1]), (doorWidth, doorHeight)))
            pygame.draw.rect(window, brown, pygame.Rect((door2[0], door2[1]), (doorWidth, doorHeight)))
            pygame.draw.rect(window, brown, pygame.Rect((door3[0], door3[1]), (doorWidth, doorHeight)))
            pygame.display.update()
        elif runde == 3:
            window.fill((255, 255, 255))
            pygame.draw.rect(window, brown, pygame.Rect((door1[0], door1[1]), (doorWidth, doorHeight)))
            pygame.draw.rect(window, brown, pygame.Rect((door2[0], door2[1]), (doorWidth, doorHeight)))
            pygame.draw.rect(window, brown, pygame.Rect((door3[0], door3[1]), (doorWidth, doorHeight)))
            pygame.display.update()
        else:
            break
    except Exception as e:
        print(e)
        print("[ERROR] Error in the program, fix it!")
print("Bye")