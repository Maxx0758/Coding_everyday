from random import randint
import math
import pygame, sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode([800,600])

White = (255, 255, 255)

Red = (255, 0, 0)

Blue = (0, 0, 255)

running = True

Green  = (0, 255, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 30)
font2 = pygame.font.SysFont("comicsansms", 15)
text = font.render("What is the most effective transport", True, (255, 255, 255))
text2 = font2.render("Public transport", True, (255, 255, 255))
text3 = font2.render("Bike", True, (255, 255, 255))
text4 = font2.render("Car", True, (255, 255, 255))

stext = font.render("Which console is Super Smash a game for?", True, (255, 255, 255))
stext2 = font2.render("Nintendo consoles", True, (255, 255, 255))
stext3 = font2.render("Playstation", True, (255, 255, 255))
stext4 = font2.render("Xbox", True, (255, 255, 255))

ttext = font.render("Which country is Porsche getting produced in?", True, (255, 255, 255))
ttext2 = font2.render("Germany", True, (255, 255, 255))
ttext3 = font2.render("England", True, (255, 255, 255))
ttext4 = font2.render("Japan", True, (255, 255, 255))

def roundOne():
    window.fill((0,0,0))
    window.blit(text, (400 - text.get_width() // 2, 30 - text.get_height() // 2))
    window.blit(text2, (150 - text2.get_width() // 2, 75 - text2.get_height() // 2))
    window.blit(text3, (400 - text3.get_width() // 2, 75 - text3.get_height() // 2))
    window.blit(text4, (650 - text4.get_width() // 2, 75 - text4.get_height() // 2))
    pygame.display.flip()
    clock.tick(60)
    door1 = pygame.draw.rect(window, Red, Rect((50, 100),(200, 400)))
    print(door1)
    door2 = pygame.draw.rect(window, Red, Rect((300, 100),(200, 400)))
    print(door2)
    door3 = pygame.draw.rect(window, Red, Rect((550, 100),(200, 400)))
    print(door3)
    pygame.display.update()

def roundSecond():
    window.fill((0,0,0))
    window.blit(stext, (400 - stext.get_width() // 2, 30 - stext.get_height() // 2))
    window.blit(stext2, (150 - stext2.get_width() // 2, 75 - stext2.get_height() // 2))
    window.blit(stext3, (400 - stext3.get_width() // 2, 75 - stext3.get_height() // 2))
    window.blit(stext4, (650 - stext4.get_width() // 2, 75 - stext4.get_height() // 2))
    pygame.display.flip()
    clock.tick(60)
    door1 = pygame.draw.rect(window, Blue, Rect((50, 100),(200, 400)))
    print(door1)
    door2 = pygame.draw.rect(window, Blue, Rect((300, 100),(200, 400)))
    print(door2)
    door3 = pygame.draw.rect(window, Blue, Rect((550, 100),(200, 400)))
    print(door3)
    pygame.display.update()

def roundThird():
    window.fill((0,0,0))
    window.blit(ttext, (400 - ttext.get_width() // 2, 30 - ttext.get_height() // 2))
    window.blit(ttext2, (150 - ttext2.get_width() // 2, 75 - ttext2.get_height() // 2))
    window.blit(ttext3, (400 - ttext3.get_width() // 2, 75 - ttext3.get_height() // 2))
    window.blit(ttext4, (650 - ttext4.get_width() // 2, 75 - ttext4.get_height() // 2))
    pygame.display.flip()
    clock.tick(60)
    door1 = pygame.draw.rect(window, Green, Rect((50, 100),(200, 400)))
    print(door1)
    door2 = pygame.draw.rect(window, Green, Rect((300, 100),(200, 400)))
    print(door2)
    door3 = pygame.draw.rect(window, Green, Rect((550, 100),(200, 400)))
    print(door3)
    pygame.display.update()

while(running):
    try:
        mousePos = pygame.mouse.get_pos()
        print(mousePos)
        pygame.time.delay(100)
        runde = True

        if runde == True:
            roundOne()

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
                        print("Når når du er pro, første spørgsmål korrekt.")
                        andenRunde = True
                        runde = False
                        break

        
        if andenRunde == True:
            
            roundSecond()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if door1.collidepoint(mousePos):
                        print("Når når du er pro, anden spørgsmål korrekt.")
                        tredjeRunde = True
                        andenRunde = False
                        break
                    elif door2.collidepoint(mousePos):
                        print("Forkert noob")
                        tredjeRunde = True
                        running = False
                        break
                    elif door3.collidepoint(mousePos):
                        print("Forkert noob")
                        tredjeRunde = True
                        running = False
                        break

        if tredjeRunde == True:

            roundThird()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if door1.collidepoint(mousePos):
                        print("Når når du er pro, tredje spørgsmål er korrekt.")
                        running = False
                        break
                    elif door2.collidepoint(mousePos):
                        print("Forkert noob")
                        running = False
                        break
                    elif door3.collidepoint(mousePos):
                        print("Forkert noob")
                        running = False
                        break

    except Exception as e:
        print(e)
        print("Unknown error")

print("\n Tak for spillet")

        