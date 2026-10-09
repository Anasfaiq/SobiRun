import json
import pygame

class TextBox:
    def __init__(self, q_id="q"):
        #load data dari json
        self.data = self.load_data(q_id)
        self.font = pygame.font.Font('assets/fonts/Silkscreen/Silkscreen-Regular.ttf', 20)
        self.text_color = (255, 255, 255)
        self.box_color = (30, 30, 30)

        #posisi
        self.rect = pygame.Rect(50,400,700,150)

    def load_data(self, q_id):
        with open("assets/questions.json","r") as f:
            all_questions = json.load(f)[0]["questions"]
            #kalo id ga ketemu , langsung ke soal pertama
        return all_questions.get(q_id, all_questions["pertanyaan 1"])

    def draw(self,screen):
        #gambar kotak petanyaan
        pygame.draw.rect(screen, self.box_color, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)

        max_width = self.rect.width - 20
        y = self.rect.y + 10

        # pertanyaan (dengan word wrap)
        for line in self.wrap_text(self.data["q"], max_width):
            surf = self.font.render(line, True, self.text_color)
            screen.blit(surf, (self.rect.x + 10, y))
            y += 26

        y += 10  # jarak antara pertanyaan dan opsi

        # pilihan jawaban
        for option in self.data["options"]:
            surf = self.font.render(option, True, self.text_color)
            screen.blit(surf, (self.rect.x + 10, y))
            y += 26
        

    