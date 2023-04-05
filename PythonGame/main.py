import pygame

from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)

# Init the Game
pygame.init()

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption("First Game")
playerImg = pygame.image.load('space_invaders.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 370
playerY = 450


def init_rocket(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == pygame.K_UP:
                print("Entered")
                playerY -= 0.1
            elif event.key == pygame.K_DOWN:
                 playerY += 0.1
            elif event.key == pygame.K_RIGHT:
                 playerX += 0.1
            elif event.key == pygame.K_LEFT:
                playerX -= 0.1

            elif event.key == K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))

    init_rocket(playerX, playerY)

    pygame.display.update()