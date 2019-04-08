import pygame
from random import randint

#Initialises the Pygame module
pygame.init()

#Sizes of the different things
(width, height) = (1500, 800)
(doorWidth, doorHeight) = (200, 400)
door1 = (100, 200)
door2 = ((width / 2) - (doorWidth / 2), 200)
door3 = (1200, 200)
(doorHandleHeight, doorHandleWidth) = (9, 35)
(doorWindowHeight, doorWindowWidth) = (50, 50)
running = True
Round = 1
brown = (102, 51, 0)
black = (0, 0, 0)
windowColor = (158, 219, 224)
background = (255, 255, 255)
#Questions and answers
questions = ["hej med dig", "Test 2", "Test 3", "Test 4"]


window = pygame.display.set_mode((width,height))
pygame.display.set_caption("The doors")

headlineFont = pygame.font.SysFont("comicsansms", 30, False, False)
def startup():
    drawRound1()

def drawRound1():
    window.fill(background)
    #Door 1
    pygame.draw.rect(window, brown, pygame.Rect((door1[0], door1[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door1[0] + doorWidth) - doorHandleWidth - 15, ((door1[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door1[0] + (doorWidth / 2) - (doorWindowWidth / 2), door1[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Door 2
    pygame.draw.rect(window, brown, pygame.Rect((door2[0], door2[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door2[0] + doorWidth) - doorHandleWidth - 15, ((door2[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door2[0] + (doorWidth / 2) - (doorWindowWidth / 2), door2[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Door 3
    pygame.draw.rect(window, brown, pygame.Rect((door3[0], door3[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door3[0] + doorWidth) - doorHandleWidth - 15, ((door3[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door3[0] + (doorWidth / 2) - (doorWindowWidth / 2), door3[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Question
    drawHeadline1()
    pygame.display.update()

def drawRound2():
    window.fill(background)
    #Door 1
    pygame.draw.rect(window, brown, pygame.Rect((door1[0], door1[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door1[0] + doorWidth) - doorHandleWidth - 15, ((door1[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door1[0] + (doorWidth / 2) - (doorWindowWidth / 2), door1[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Door 2
    pygame.draw.rect(window, brown, pygame.Rect((door2[0], door2[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door2[0] + doorWidth) - doorHandleWidth - 15, ((door2[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door2[0] + (doorWidth / 2) - (doorWindowWidth / 2), door2[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Door 3
    pygame.draw.rect(window, brown, pygame.Rect((door3[0], door3[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door3[0] + doorWidth) - doorHandleWidth - 15, ((door3[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door3[0] + (doorWidth / 2) - (doorWindowWidth / 2), door3[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Question
    drawHeadline1()
    pygame.display.update()

def drawRound3():
    window.fill(background)
    #Door 1
    pygame.draw.rect(window, brown, pygame.Rect((door1[0], door1[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door1[0] + doorWidth) - doorHandleWidth - 15, ((door1[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door1[0] + (doorWidth / 2) - (doorWindowWidth / 2), door1[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Door 2
    pygame.draw.rect(window, brown, pygame.Rect((door2[0], door2[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door2[0] + doorWidth) - doorHandleWidth - 15, ((door2[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door2[0] + (doorWidth / 2) - (doorWindowWidth / 2), door2[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Door 3
    pygame.draw.rect(window, brown, pygame.Rect((door3[0], door3[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door3[0] + doorWidth) - doorHandleWidth - 15, ((door3[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door3[0] + (doorWidth / 2) - (doorWindowWidth / 2), door3[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Question
    drawHeadline1()
    pygame.display.update()

def drawRound4():
    window.fill(background)
    #Door 1
    pygame.draw.rect(window, brown, pygame.Rect((door1[0], door1[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door1[0] + doorWidth) - doorHandleWidth - 15, ((door1[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door1[0] + (doorWidth / 2) - (doorWindowWidth / 2), door1[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Door 2
    pygame.draw.rect(window, brown, pygame.Rect((door2[0], door2[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door2[0] + doorWidth) - doorHandleWidth - 15, ((door2[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door2[0] + (doorWidth / 2) - (doorWindowWidth / 2), door2[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Door 3
    pygame.draw.rect(window, brown, pygame.Rect((door3[0], door3[1]), (doorWidth, doorHeight)))
    pygame.draw.ellipse(window, black, pygame.Rect(((door3[0] + doorWidth) - doorHandleWidth - 15, ((door3[1]) + (doorHeight / 2)) - 20), (doorHandleWidth, doorHandleHeight)))
    pygame.draw.rect(window, windowColor, pygame.Rect((door3[0] + (doorWidth / 2) - (doorWindowWidth / 2), door3[1] + doorWindowHeight), (doorWindowWidth, doorWindowHeight)))
    #Question
    drawHeadline1()
    pygame.display.update()

def drawHeadline1():
    i = randint(0, len(questions) - 1)
    question = headlineFont.render(questions[i], True, black)
    questions.pop(i)
    window.blit(question, ((width / 2) - question.get_width() // 2, 30 - question.get_height() // 2))
    
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
                        drawRound4()
                    elif Round == 4:
                        running = False
                elif 650 <= mousePos[0] <= 850 and 200 <= mousePos[1] <= 600:
                    if Round == 1:
                        Round = 2
                        drawRound2()
                    elif Round == 2:
                        Round = 3
                        drawRound3()
                    elif Round == 3:
                        drawRound4()
                    elif Round == 4:
                        running = False
                elif 1200 <= mousePos[0] <= 1400 and 200 <= mousePos[1] <= 600:
                    if Round == 1:
                        Round = 2
                        drawRound2()
                    elif Round == 2:
                        Round = 3
                        drawRound3()
                    elif Round == 3:
                        drawRound4()
                    elif Round == 4:
                        running = False
            break
    except Exception as e:
        print(e)
        print("[ERROR] Error in the program, fix it!")
print("Bye")