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
        pygame.time.delay(100)
        pygame.display.set_caption("The doors")
        mousePos = pygame.mouse.get_pos()
        print(mousePos)
        print(runde)
        #Looking for alle the events, thats happening
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 100 <= mousePos[0] <= 300 and 200 <= mousePos[1] <= 600:
                    if runde == 1:
                        runde = 2
                    elif runde == 2:
                        runde = 3
                    elif runde == 3:
                        running = False
                elif 650 <= mousePos[0] <= 850 and 200 <= mousePos[1] <= 600:
                    if runde == 1:
                        runde = 2
                    elif runde == 2:
                        runde = 3
                    elif runde == 3:
                        running = False
                elif 1200 <= mousePos[0] <= 1400 and 200 <= mousePos[1] <= 600:
                    if runde == 1:
                        runde = 2
                    elif runde == 2:
                        runde = 3
                    elif runde == 3:
                        running = False
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