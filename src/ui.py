import pygame
from src.config import TITLE_SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH

class UI:
    def __init__(self):
        self.small_font = pygame.font.Font('assets/fonts/Silkscreen/Silkscreen-Regular.ttf', 40)
        self.big_font = pygame.font.Font('assets/fonts/Silkscreen/Silkscreen-Bold.ttf', 60)
        self.title_bg = pygame.image.load(TITLE_SCREEN).convert()

        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

    def main_menu(self, screen):
        x = (SCREEN_WIDTH - self.title_bg.get_width()) // 2
        y = (SCREEN_HEIGHT - self.title_bg.get_height()) // 4
        
        screen.blit(self.title_bg, (x, y))

        start_surf = self.small_font.render("Tekan Space untuk Mulai", False, self.white)
        start_rect = start_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100))

        screen.blit(start_surf, start_rect)

    def draw_score(self, screen, score, high_score):
        score_surf = self.small_font.render(f"Score: {score}", False, self.white)
        high_score_surf = self.small_font.render(f"High Score: {high_score}", False, self.white)

        score_rect = score_surf.get_rect(topright = (SCREEN_WIDTH - 20, 20))
        high_score_rect = high_score_surf.get_rect(topright = (SCREEN_WIDTH - 20, 50))

        screen.blit(score_surf, score_rect)
        screen.blit(high_score_surf, high_score_rect)

    def game_over(self, screen, score, high_score):
        game_over_surf = self.big_font.render("GAME OVER", False, self.red)
        score_surf = self.small_font.render(f"Score Akhir: {score}", False, self.white)
        high_score_surf = self.high_score.render(f"High Score: {high_score}", False, self.white)
        restart_surf = self.small_font.render("Tekan R untuk Ulangi", False, self.white)

        game_over_rect = game_over_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100))
        score_rect = score_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        high_score_rect = high_score_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
        restart_rect = restart_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))

        screen.blit(game_over_surf, game_over_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(high_score_surf, high_score_rect)
        screen.blit(restart_surf, restart_rect)