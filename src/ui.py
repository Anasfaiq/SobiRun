import pygame
from src.config import TITLE_SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH

class UI:
    def __init__(self):
        # ngatur font dan ukuran font disini
        self.small_font = pygame.font.Font('assets/fonts/Silkscreen/Silkscreen-Regular.ttf', 20)
        self.big_font = pygame.font.Font('assets/fonts/Silkscreen/Silkscreen-Bold.ttf', 60)

        # buat ngeload title
        original_image = pygame.image.load(TITLE_SCREEN).convert()

        # buat mengatur size title di main menu
        self.title_bg = pygame.transform.scale(original_image, (original_image.get_width() // 5, original_image.get_height() // 5))

        # biar kalo perlu warna tinggal manggil variable di bawah ini dan gaperlu ngetik hex nya lagi
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

    def main_menu(self, screen):
        # buat mengatur posisi title
        x = (SCREEN_WIDTH - self.title_bg.get_width()) // 2
        y = (SCREEN_HEIGHT - self.title_bg.get_height()) // 4

        # me-render title 
        screen.blit(self.title_bg, (x, y))

        # membuat dan me-render text
        start_surf = self.small_font.render("Tekan Space untuk Mulai", False, self.white)
        start_rect = start_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100))
        screen.blit(start_surf, start_rect)

    def draw_score(self, screen, score, high_score):
        # render teks score ke surface
        score_surf = self.small_font.render(f"Score: {score}", False, self.white)
        high_score_surf = self.small_font.render(f"High Score: {high_score}", False, self.white)

        # mengambil posisi dari kedua surface dan menyimpan nya ke variabel agar bisa di pakai di blit
        score_rect = score_surf.get_rect(topright = (SCREEN_WIDTH - 20, 20))
        high_score_rect = high_score_surf.get_rect(topright = (SCREEN_WIDTH - 20, 50))

        # menampilkan teks ke layar
        screen.blit(score_surf, score_rect)
        screen.blit(high_score_surf, high_score_rect)

    def game_over(self, screen, score, high_score):
        # me-render teks ke surface
        game_over_surf = self.big_font.render("GAME OVER", False, self.red)
        score_surf = self.small_font.render(f"Score Akhir: {score}", False, self.white)
        high_score_surf = self.small_font.render(f"High Score: {high_score}", False, self.white)
        restart_surf = self.small_font.render("Tekan R untuk Ulangi", False, self.white)
        menu_surf = self.small_font.render("Tekan M untuk Main Menu",False, self.white)

        # mengambil posisi dan menyimpan nya ke variabel agar bisa di pakai di blit
        game_over_rect = game_over_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100))
        score_rect = score_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        high_score_rect = high_score_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
        restart_rect = restart_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))
        menu_rect = menu_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150))

        # menampilkan teks ke layar
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(high_score_surf, high_score_rect)
        screen.blit(restart_surf, restart_rect)
        screen.blit(menu_surf, menu_rect)