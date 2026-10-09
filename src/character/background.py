import json
import pygame
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT


class Background:
    def __init__(self, background_id="background", speed=2):
        # load data dari json
        self.data = self.load_data(background_id)

        # load gambar background
        image = pygame.image.load(self.data["sprites"]).convert()
        self.image = pygame.transform.smoothscale(image, (SCREEN_WIDTH,SCREEN_HEIGHT))

        # ukuran gambar
        self.width = self.image.get_width()

        # posisi 2 gambar (biar nyambung pas scrolling)
        self.x1 = 0
        self.x2 = self.width

        # kecepatan scroll
        self.speed = speed

    def load_data(self, bg_id):
        with open("assets/assets.json", "r") as f:
            items = json.load(f)
            for item in items:
                if item["id"] == bg_id:
                    return item
        return items[0]

    def update(self):
        # geser ke kiri
        self.x1 -= self.speed
        self.x2 -= self.speed

        # kalo satu gambar udah keluar layar, pindahin ke belakang gambar satunya
        if self.x1 <= -self.width:
            self.x1 = self.x2 + self.width
        if self.x2 <= -self.width:
            self.x2 = self.x1 + self.width

    def draw(self, screen):
        screen.blit(self.image, (self.x1, 0))
        screen.blit(self.image, (self.x2, 0))