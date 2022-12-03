import pygame
from config import PARAMS
from sonar import Sonar


def get_font(size):
    return pygame.font.Font("assets/airstrike.ttf", size)


def create_wall(pos, state, grid, w, h):
    i = pos[0] // w
    j = pos[1] // h
    grid[i][j].wall = state


def create_grid():
    grid = []
    for i in range(PARAMS["cols"]):
        arr = []
        for j in range(PARAMS["rows"]):
            sonar = Sonar(i, j)
            arr.append(sonar)
        grid.append(arr)
    return grid


def fill_grid(grid):
    for i in range(PARAMS["cols"]):
        for j in range(PARAMS["rows"]):
            grid[i][j].add_neighbors(grid)
    return grid
