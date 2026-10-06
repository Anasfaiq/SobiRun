import json
import os

class ScoreManager :

    def __init__(self, filepath="highscore.json"):
        self.filepath = filepath
        self.score = 0 #skor berjalan saat main
        self.high_score = self.load_high_score() #skor tertinggi 
        self.score_speed = 0.1 #kecepatan penambahan skor tiap frame

    def update(self):
        """Menambahkan skor berjalan seiring waktu permainan."""
        self.score += self.score_speed

        #Jika skor melewati high score, langsung perbarui high score 
        if self.score > self.high_score:
            self.high_score = self.score

    def on_game_over(self):
        """Di panggil saat Dino menabrak rintangan / Game Over. """
        self.save_high_score()

    def reset_score(self):
        """Di panggil saat pemain berhasil menjawab kuis dan memulai ulang permainan."""
        self.score = 0

    def get_score_int(self):
        """Mengembalikan skor saat ini dalam bentuk angka bulat (integer)."""
        return int(self.score)

    def get_high_score_int(self):
        """Mengembalikan high score dalam bentuk angka bulat (integer)."""
        return int(self.high_score)

    def load_high_score(self):
        """Membaca high score dari file json"""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    data = json.load(f)
                    return data.get("high_score",0)
            except(json.JSONDecodeError, IOError):
                return 0
        return 0

    def save_high_score(self):
        """Menyimpan high score ke file json agar tidak hilang saat game ditutup."""
        try:
            with open(self.filepath, "w") as f:
                json.dump({"high_score": self.high_score},f)
        except IOError as e:
            print(f"Gagal menyimpan high score {e}")