import pygame
from random import randint
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT


class Obstacles:
    # semua ukuran relatif terhadap kanvas, acuan desain 1920x1080
    SCALE = SCREEN_HEIGHT / 1080

    # garis tanah (posisi bawah obstacle). Dari kodemu: 765 + 40 = 805
    GROUND_Y = int(805 * SCALE)

    def __init__(self):
        self.jenis = randint(1, 3)
        self.x = SCREEN_WIDTH
        self.speed = 15 * (SCREEN_WIDTH / 1920)

        if self.jenis == 1:
            self.width = int(40 * self.SCALE)
            self.height = int(40 * self.SCALE)
            self.color = (0, 0, 139)
        elif self.jenis == 2:
            self.width = int(30 * self.SCALE)
            self.height = int(80 * self.SCALE)
            self.color = (255, 200, 50)
        elif self.jenis == 3:
            self.width = int(40 * self.SCALE)
            self.height = int(30 * self.SCALE)
            self.color = (200, 50, 255)

        # semua obstacle berdiri di garis tanah yang sama
        self.y = self.GROUND_Y - self.height
        self.rect = pygame.Rect(int(self.x), self.y, self.width, self.height)

    def move(self):
        self.x -= self.speed
        self.rect.x = int(self.x)

    def get_hitbox(self):
        return self.rect

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)