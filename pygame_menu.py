import pygame
from config import PARAMS
import utils
import sys
from button import Button

pygame.init()
pygame.display.set_caption("Dijkstra's Sonar")

# Set screen size and image background
SCREEN = pygame.display.set_mode((PARAMS["width_screen"], PARAMS["height_screen"]))
BG = pygame.image.load("assets/submarine_background.jpg")

# Load music game
pygame.mixer.music.load('assets/Sneaky-Snitch.mp3')
pygame.mixer.music.play(-1)

def play():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = utils.get_font(45).render("PLAY SCREEN", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=utils.get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.change_color(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.check_for_input(OPTIONS_MOUSE_POS):
                    main_menu()

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


