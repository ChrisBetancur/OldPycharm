import pygame

from Model.cell import Cell, Pixel, change_state, ACTIVE_COLOR
from Util.CellularState import State


class World:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.matrix = []

        self.init_world()

    def init_world(self):
        for row in range(self.rows):
            new_col = []
            for col in range(self.columns):
                cell = Cell(row, col)
                new_col.append(cell)
            self.matrix.append(new_col)

    def highlight_row(self, input):
        for row in self.matrix:
            for cell in row:
                if cell.matrix_row == input:
                    cell.state = State.ACTIVE


class Display:
    def __init__(self, world, cell_size, width, height):
        self.x_offset = cell_size[0]
        self.y_offset = cell_size[1]

        self.width = width
        self.height = height

        self.rows = world.rows
        self.columns = world.columns

        self.world = world
        self.pixel_list = []

        for row in world.matrix:
            for cell in row:
                pixel = Pixel(cell, (self.x_offset, self.y_offset), command=change_state)
                self.pixel_list.append(pixel)

        self.init_matrix()

    def init_matrix(self):
        index = 0
        for y_pos in range(0, self.height, self.y_offset):
            for x_pos in range(0, self.width, self.x_offset):
                self.pixel_list[index].set_pos(x_pos, y_pos)
                index += 1

    def get_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return
        for pixel in self.pixel_list:
            pixel.get_event(event)
        self.update()

    def update(self):
        for pixel in self.pixel_list:
            if pixel.cell.state == State.ACTIVE:
                pixel.color = ACTIVE_COLOR

    def draw(self, surf, world):
        for pixel in self.pixel_list:
            pixel.draw(surf, world)
