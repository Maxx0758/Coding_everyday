import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First game")

X = 50
Y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        X -= vel
    if keys[pygame.K_RIGHT]:
        X += vel
    if keys[pygame.K_UP]:
        Y -= vel
    if keys[pygame.K_DOWN]:
        Y += vel
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (X, Y, width, height))
    pygame.display.update()
    
pygame.QUIT()