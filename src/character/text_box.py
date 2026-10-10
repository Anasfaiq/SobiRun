import json
import pygame
from src.config import SCREEN_HEIGHT

class TextBox:
    def __init__(self, q_id="q"):
        #load data dari json
        self.data = self.load_data(q_id)
        self.font = pygame.font.Font('assets/fonts/Silkscreen/Silkscreen-Regular.ttf', 15)
        self.text_color = (255, 255, 255)
        self.box_color = (30, 30, 30)

        self.padding = 10
        self.gap = 10
        self.line_height = self.font.get_linesize() + 4

        #posisi
        self.rect = pygame.Rect(50,0,700,150)
        max_width = self.rect.width - self.padding * 2

        # wrap text
        self.q_lines = self.wrap_text(self.data["q"], max_width)
        self.option_lines = []
        for option in self.data["options"]:
            self.option_lines.extend(self.wrap_text(option, max_width))

        # tinggi kotak menyesuaikan dengan isi
        total_lines = len(self.q_lines) + len(self.option_lines)
        needed = self.padding * 2 + total_lines * self.line_height + self.gap
        self.rect.height = max(150, needed)
        self.rect.bottom = SCREEN_HEIGHT - 20

    def load_data(self, q_id):
        with open("assets/questions.json","r") as f:
            all_questions = json.load(f)[0]["questions"]
            #kalo id ga ketemu , langsung ke soal pertama
        return all_questions.get(q_id, all_questions["pertanyaan 1"])

    def is_correct(self, index):
        return index == self.data["correct"]

    def wrap_text(self, text, max_width):
        words = text.split(" ")
        lines = []
        current_line = ""
        for word in words:
            test_line = f"{current_line} {word}".strip()
            # cek lebar teks kalo ditambah kata ini
            if self.font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    def draw(self,screen):
        #gambar kotak petanyaan
        pygame.draw.rect(screen, self.box_color, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)

        y = self.rect.y + self.padding

        for line in self.q_lines:
            screen.blit(self.font.render(line, True, self.text_color), (self.rect.x + self.padding, y))
            y += self.line_height

        # jarak antara pertanyaan dan opsi
        y += self.gap

        # pilihan jawaban
        for line in self.option_lines:
            screen.blit(self.font.render(line, True, self.text_color), (self.rect.x + self.padding, y))
            y += self.line_height
        

    