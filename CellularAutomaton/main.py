import pygame

from Model.matrix import World, Display
from Util.CellularState import State

ROWS = 200
COLUMNS = 200
PIXEL_SIZE = 5

WINDOW_WIDTH = COLUMNS * PIXEL_SIZE
WINDOW_HEIGHT = ROWS * PIXEL_SIZE

pygame.init()

world = World(ROWS, COLUMNS)
# world.highlight_row(199)
display = Display(world, (PIXEL_SIZE, PIXEL_SIZE), WINDOW_WIDTH, WINDOW_HEIGHT)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill((0, 0, 0))


def draw_window():
    display.draw(screen, world)


def init_window():
    running = True

    while running:
        for event in pygame.event.get():
            if event is pygame.QUIT:
                running = False
            display.get_event(event)
        draw_window()
        pygame.display.update()


init_window()
