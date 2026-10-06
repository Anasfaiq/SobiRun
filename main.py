import pygame
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True 
while running :
    #ketika menjalan kan gamenya 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)

    pygame.display.set_caption(TITLE)

pygame.quit()