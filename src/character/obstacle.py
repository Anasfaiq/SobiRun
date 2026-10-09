import pygame
from random import randint

class Obstacles:
    def __init__(self):
        self.jenis = randint(1,3)
        self.x = 1920
        self.speed = 15

        if self.jenis == 1:
            self.width = 40
            self.height = 40
            self.y = 765
            self.color = (0, 0, 139)
        elif self.jenis == 2:
            self.width = 30
            self.height = 80
            self.y = 722
            self.color = (255, 200, 50)
        elif self.jenis == 3:
            self.width = 40
            self.height = 30
            self.y = 772
            self.color = (200, 50, 255)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.x -= self.speed
        self.rect.x = self.x

    def get_hitbox(self):
        return self.rect
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

