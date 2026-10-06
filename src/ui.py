import pygame
from src.config import TITLE_SCREEN

class UI:
    def __init__(self):
        self.small_font = pygame.font.Font('assets/fonts/Silkscreen/Silkscreen-Regular.ttf', 40)
        self.big_font = pygame.font.Font('assets/fonts/Silkscreen/Silkscreen-Bold.ttf', 60)

    def main_menu(self):
        self.title = TITLE_SCREEN
        