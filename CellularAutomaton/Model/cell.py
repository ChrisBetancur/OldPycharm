import time

import pygame

from Attributes.cell_attributes import validate_position
from Model.Materials.MaterialPhysics.Physics import apply_gravity
from Util.CellularState import State

ACTIVE_COLOR = (255, 255, 255)
EMPTY_COLOR = (0, 0, 0)


class Cell:
    def __init__(self, row, col, state=State.EMPTY):
        self.matrix_row = row
        self.matrix_col = col

        self.particle = None

        self.state = state

    def determine_radius(self, world):
        curr_row = self.matrix_row
        curr_col = self.matrix_col
        cells = []

        # Below first
        if validate_position(curr_row + 1, curr_col, world):
            cells.append(world.matrix[curr_row + 1][curr_col])

        if validate_position(curr_row + 1, curr_col - 1, world):
            cells.append(world.matrix[curr_row + 1][curr_col - 1])

        if validate_position(curr_row, curr_col - 1, world):
            cells.append(world.matrix[curr_row][curr_col - 1])

        if validate_position(curr_row - 1, curr_col - 1, world):
            cells.append(world.matrix[curr_row - 1][curr_col - 1])

        if validate_position(curr_row - 1, curr_col, world):
            cells.append(world.matrix[curr_row - 1][curr_col])

        if validate_position(curr_row - 1, curr_col + 1, world):
            cells.append(world.matrix[curr_row - 1][curr_col + 1])

        if validate_position(curr_row, curr_col + 1, world):
            cells.append(world.matrix[curr_row][curr_col + 1])

        if validate_position(curr_row + 1, curr_col + 1, world):
            cells.append(world.matrix[curr_row + 1][curr_col + 1])

        return cells


class Pixel:
    def __init__(self, cell, size, command=None):
        self.cell = cell
        self.function = command

        self.x_pos = 0
        self.y_pos = 0

        self.size = size

        self.color = EMPTY_COLOR

        if cell.state is State.ACTIVE:
            self.color = ACTIVE_COLOR

        self.rect = None

    def set_pos(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = pygame.Rect((self.x_pos, self.y_pos), self.size)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.function(self)

    def draw(self, surf, world):
        pygame.draw.rect(surf, self.color, self.rect)
        if self.cell.state == State.ACTIVE:
            # apply_gravity(self.cell, world)
            pygame.draw.rect(surf, self.color, self.rect)


def change_state(pixel):
    pixel.cell.state = State.ACTIVE
