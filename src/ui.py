import pygame
import json
from src.config import TITLE_SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH

class UI:
    def __init__(
            self, 
            background_id="background", 
            quit_id= "quit_button_menu",
            mulai_id= "menu_button",
            volume_id= "volume_button_simbol"
        ):
        # ngatur font dan ukuran font disini
        self.small_font = pygame.font.Font('assets/fonts/Silkscreen/Silkscreen-Regular.ttf', 20)
        self.big_font = pygame.font.Font('assets/fonts/Silkscreen/Silkscreen-Bold.ttf', 60)
        self.scale = 2.5

        #background bsi
        self.data = self.load_data(background_id)
        image = pygame.image.load(self.data["sprites"]).convert()
        self.image = pygame.transform.smoothscale(image, (SCREEN_WIDTH,SCREEN_HEIGHT))

        #tombol mulai dan keluar dan volume
        self.data = self.load_data(mulai_id)
        sprites_info = self.data["sprites"]
        self.frames_start = self.load_sprite_sheet(
            sprites_info["start"]["file"], sprites_info["start"]["frame_count"], self.scale
        )

        self.data = self.load_data(quit_id)
        sprites_info = self.data["sprites"]
        self.frames_quit = self.load_sprite_sheet(
            sprites_info["quit"]["file"], sprites_info["quit"]["frame_count"], self.scale
        )

        self.data = self.load_data(volume_id)
        sprites_info = self.data["sprites"]
        self.frames_volume = self.load_sprite_sheet(
            sprites_info["volume"]["file"], sprites_info["volume"]["frame_count"], self.scale
        )
        

        # buat ngeload title
        original_image = pygame.image.load(TITLE_SCREEN).convert_alpha()

        # buat mengatur size title di main menu
        self.title_bg = pygame.transform.scale(original_image, (original_image.get_width() // 2, original_image.get_height() // 2))

        # biar kalo perlu warna tinggal manggil variable di bawah ini dan gaperlu ngetik hex nya lagi
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

    def load_data(self, bg_id):
        with open("assets/assets.json", "r") as f:
            items = json.load(f)
            for item in items:
                if item.get("id") == bg_id:
                    return item
        return items[0]

    def load_sprite_sheet(self, filepath, frame_count, scale=1.0):
        sheet = pygame.image.load(filepath).convert_alpha()
        sheet_width = sheet.get_width()
        sheet_height = sheet.get_height()

        frame_width = sheet_width // frame_count
        frames = []

        for i in range(frame_count):
            rect = pygame.Rect(i * frame_width, 0, frame_width, sheet_height)
            frame = sheet.subsurface(rect)

            # buat ubah ukuran
            new_size = (int(frame_width * scale), int(sheet_height * scale))
            frame = pygame.transform.scale(frame, new_size)

            frames.append(frame)

        return frames

    def main_menu(self, screen):
        # buat ngatur posisi tombol dan title
        start_img = self.frames_start[0]
        quit_img = self.frames_quit[0]
        volume_img = self.frames_volume[0]

        center_x = SCREEN_WIDTH // 2
        gap = 20  # jarak antar elemen

        # title: di tengah atas
        title_rect = self.title_bg.get_rect(center=(center_x, SCREEN_HEIGHT // 2.2))

        # tombol start: tepat di bawah title
        start_rect = start_img.get_rect(midtop=(center_x, title_rect.bottom + gap))

        # tombol quit: tepat di bawah tombol start
        quit_rect = quit_img.get_rect(midtop=(center_x, start_rect.bottom))

        # tombol volume: pojok kanan bawah
        volume_rect = volume_img.get_rect(bottomright=(SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20))

        # me-render title 
        screen.blit(self.image, (0,0))
        screen.blit(self.title_bg, title_rect)
        screen.blit(start_img, start_rect)
        screen.blit(quit_img, quit_rect)
        screen.blit(volume_img, volume_rect)
        

        # membuat dan me-render text
        start_surf = self.small_font.render("Tekan Space untuk Mulai", False, self.white)
        # exit_surf = self.small_font.render("Exit", False, self.white)
        start_text_rect = start_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))
        # exit_rect = exit_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT + 100))
        screen.blit(start_surf, start_text_rect)
        # screen.blit(exit_surf, exit_rect)

    def draw_score(self, screen, score, high_score):
        # render teks score ke surface
        self.choclate = (60, 42, 26) 
        score_surf = self.small_font.render(f"Score: {score}", False, self.choclate)
        high_score_surf = self.small_font.render(f"High Score: {high_score}", False, self.choclate)

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