import pygame

# --- constants --- (UPPER_CASE_NAMES)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 25

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

# --- main ---

pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

surface = pygame.surface.Surface(screen.get_size()).convert_alpha()
surface.fill([0,0,0,0])
pygame.draw.polygon(surface, WHITE, [(100,100), (200,200), (300,100)])

clock = pygame.time.Clock()

running = True
while running:

    # --- events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False

    # --- draws ---

    screen.fill(GREEN)

    screen.blit(surface, (0,0))

    pygame.display.flip()

    # --- FPS ---

    ms = clock.tick(FPS)
    #pygame.display.set_caption('{}ms'.format(ms)) # 40ms for 25FPS, 16ms for 60FPS
    fps = clock.get_fps()
    pygame.display.set_caption('FPS: {}'.format(fps))

# --- end ---

pygame.quit()