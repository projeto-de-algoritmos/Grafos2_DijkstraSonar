import pygame
from config import PARAMS


w = PARAMS["width_screen"] // PARAMS["cols"]
h = PARAMS["height_screen"] // PARAMS["rows"]


class Sonar:
    def __init__(self, i, j):
        self.IMAGE = pygame.image.load('assets/submarine_2.png').convert_alpha()
        self.x = i
        self.y = j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False
        if (i + j) % 7 == 0:
            self.wall = True

    def show(self, win, col, shape=1):
        if self.wall:
            col = (0, 0, 0)
        elif shape == 1:
            rect = self.IMAGE.get_rect()
            rect.center = (self.x * w, self.y * h)
            win.blit(self.IMAGE, rect)
        else:
            pygame.draw.circle(win, col, (self.x * w + w // 2, self.y * h + h // 2), w // 3)

    def add_neighbors(self, grid):
        if self.x < PARAMS["cols"] - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < PARAMS["rows"] - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])