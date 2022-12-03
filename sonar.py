import pygame
import random
from config import PARAMS


w = PARAMS["width_screen"] // PARAMS["cols"]
h = PARAMS["height_screen"] // PARAMS["rows"]


class Sonar:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False
        if random.randint(0, 100) < 2:
            self.wall = True

    def show(self, win, col, shape=1):
        if self.wall:
            col = (0, 0, 0)
        if shape == 1:
            pygame.draw.rect(win, col, (self.x * w, self.y * h, w - 1, h - 1))
        # Add submarine
        elif shape == 2:
            submarine_image = pygame.image.load('assets/submarine_1.png').convert_alpha()
            rect = submarine_image.get_rect()
            rect.center = (self.x * w + w // 4, self.y * h + h // 4)
            win.blit(submarine_image, rect)
        # Add enemy
        elif shape == 3:
            submarine_image = pygame.image.load('assets/submarine_3.png').convert_alpha()
            rect = submarine_image.get_rect()
            rect.center = (self.x * w + w // 4, self.y * h + h // 4)
            win.blit(submarine_image, rect)
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
