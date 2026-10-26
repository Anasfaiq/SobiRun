import json
import pygame
from random import choice
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT


class Obstacles:
    # semua ukuran relatif terhadap kanvas, acuan desain 1920x1080
    SCALE = SCREEN_HEIGHT / 1080

    # garis tanah (posisi bawah obstacle). Dari kodemu: 765 + 40 = 805
    GROUND_Y = int(805 * SCALE)

    ASSETS_DATA = {}
    CACHED_IMAGES = {}

    @classmethod
    def load_data(self):
            with open("assets/assets.json","r") as f:
                obstacles = json.load(f)
                for obstacle in obstacles:
                    if "obstacles" in obstacle:
                        self.ASSETS_DATA = obstacle["obstacles"]
                        break
            for car_key, car_info in self.ASSETS_DATA.items():
                self.CACHED_IMAGES[car_key] = pygame.image.load(car_info["path"]).convert_alpha()

    def __init__(self):
        car_keys = list(self.ASSETS_DATA.keys())
        chosen_car_key = choice(car_keys)
        car_info = self.ASSETS_DATA[chosen_car_key]

        variant = choice(car_info["variants"])

        sprite_sheet = self.CACHED_IMAGES[chosen_car_key]

        crop_rect = pygame.Rect(variant["x"], variant["y"], variant["w"], variant["h"])
        raw_image = sprite_sheet.subsurface(crop_rect)

        flipped_image = pygame.transform.flip(raw_image, True, False)

        size_multiplier = 3.3
        self.width = int(variant["w"] * self.SCALE * size_multiplier)
        self.height = int(variant["h"] * self.SCALE * size_multiplier)
        self.image = pygame.transform.scale(flipped_image, (self.width, self.height))

        # semua obstacle berdiri di garis tanah yang sama
        self.x = SCREEN_WIDTH
        self.y = self.GROUND_Y - self.height
        self.rect = self.image.get_rect(topleft=(int(self.x), self.y))

    def move(self, speed):
        self.x -= speed
        self.rect.x = int(self.x)

    def get_hitbox(self):
        return self.rect

    def draw(self, surface):
        surface.blit(self.image, self.rect)