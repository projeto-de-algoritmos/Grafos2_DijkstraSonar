import pygame
from config import PARAMS
from collections import deque
import utils
import random
import sys
from button import Button
from tkinter import messagebox, Tk

w = PARAMS["width_screen"] // PARAMS["cols"]
h = PARAMS["height_screen"] // PARAMS["rows"]

pygame.init()
pygame.display.set_caption("Dijkstra's Sonar")

# Set screen size and image background
SCREEN = pygame.display.set_mode((PARAMS["width_screen"], PARAMS["height_screen"]))
BG = pygame.image.load("assets/submarine_background.jpg")

# Load music game
pygame.mixer.music.load('assets/Sneaky-Snitch.mp3')
pygame.mixer.music.play(-1)


def play():

    queue, visited = deque(), []
    path = []

    grid = utils.create_grid()
    grid = utils.fill_grid(grid)

    pos1_sub = random.randint(1, 63)
    pos2_sub = random.randint(1, 35)
    start = grid[pos1_sub][pos2_sub]
    end = grid[random.randint(1, 63)][random.randint(1, 35)]
    end_2 = grid[PARAMS["cols"] - PARAMS["cols"] // 3][PARAMS["rows"] - PARAMS["cols"] // 5]
    end_3 = grid[PARAMS["cols"] - PARAMS["cols"] // random.randint(1, 63)][PARAMS["rows"] - PARAMS["cols"] // random.randint(1, 35)]
    start.wall = False
    end.wall = False
    end_2.wall = False

    queue.append(start)
    start.visited = True
    no_flag = True
    start_flag = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    utils.create_wall(pygame.mouse.get_pos(), event.button == 1, grid, w, h)
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] or event.buttons[2]:
                    utils.create_wall(pygame.mouse.get_pos(), event.buttons[0], grid, w, h)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_flag = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        if start_flag:
            if len(queue) > 0:
                current = queue.popleft()
                if current == end or current == end_2 or current == end_3:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev
                for i in current.neighbors:
                    if not i.visited and not i.wall:
                        i.visited = True
                        i.prev = current
                        queue.append(i)
            else:
                if no_flag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("FIM", "Pressione ESC e inicie novamente")
                    no_flag = False
                else:
                    continue

        SCREEN.fill((0, 20, 20))
        for i in range(PARAMS["cols"]):
            for j in range(PARAMS["rows"]):
                current_pos = grid[i][j]
                current_pos.show(SCREEN, (57, 105, 161))
                if current_pos in path:
                    current_pos.show(SCREEN, (57, 105, 161))
                    current_pos.show(SCREEN, (192, 57, 43), 0)
                elif current_pos.visited:
                    current_pos.show(SCREEN, (57, 105, 161))
                if current_pos in queue:
                    current_pos.show(SCREEN, (57, 105, 161))
                    current_pos.show(SCREEN, (39, 174, 96), 0)
                if current_pos == start:
                    current_pos.show(SCREEN, (0, 255, 200), shape=2)
                if current_pos == end or current_pos == end_2 or current_pos == end_3:
                    current_pos.show(SCREEN, (255, 0, 0), shape=3)

        pygame.display.flip()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = utils.get_font(80).render("Dijkstra's Sonar", True, "#C64343")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=utils.get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 450),
                             text_input="QUIT", font=utils.get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main_menu()


