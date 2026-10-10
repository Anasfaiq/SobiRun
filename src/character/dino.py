import json 
import pygame
from src.config import SCREEN_HEIGHT

class Sobi:
    def __init__(self, char_id="sobiChar"):
        #load data dari json
        self.data = self.load_data(char_id)

        #ukuran
        self.scale = 2.8

        #memotong gambar sprite
        sprites_info = self.data["sprites"]
        self.frames_run = self.load_sprite_sheet(
            sprites_info["run"]["file"], sprites_info["run"]["frame_count"], self.scale
        )
        self.frames_jump_up = self.load_sprite_sheet(
            sprites_info["jump_up"]["file"],
            sprites_info["jump_up"]["frame_count"],
            self.scale,
        )
        self.frames_jump_fall = self.load_sprite_sheet(
            sprites_info["jump_fall"]["file"],
            sprites_info["jump_fall"]["frame_count"],
            self.scale,
        )

        self.frames_died = self.load_sprite_sheet(
            sprites_info["died"]["file"],
            sprites_info["died"]["frame_count"],
            self.scale,
        )

        #animasi
        self.current_frame = 0
        self.animation_timer = 0
        # self.animation_speed = 5

        #posisi awal
        self.image = self.frames_run[0]
        self.ground_y = int(805*SCREEN_HEIGHT / 1080)
        self.rect = self.image.get_rect(bottomleft=(50, self.ground_y))

        #move / pergerakan
        self.vel_y = 0
        self.jump_power = self.data["jump_power"]
        self.gravity = self.data["gravity"]
        self.is_jumping = False
        self.is_alive = True

    def load_data(self, char_id):
        with open("assets/assets.json","r") as f:
            characters = json.load(f)
            for char in characters:
                if char["id"] == char_id:
                    return char
        return characters[0]

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

    def set_run_speed(self, speed):
        self.animation_speed = max(1,int(speed))

    def jump(self):
        if not self.is_jumping:
            self.vel_y = self.jump_power
            self.is_jumping = True
            self.current_frame = 0

    def die(self):
        if self.is_alive:
            self.is_alive = False
            self.is_jumping = False
            self.vel_y = 0
            self.current_frame = 0
            self.animation_timer = 0

    def death_finished(self):
        return not self.is_alive and self.current_frame >= len(self.frames_died) - 1

    def get_hitbox(self):
        hitbox = self.rect.inflate(-60, -40)
        hitbox.bottom = self.rect.bottom
        return hitbox

    def update(self):
        if not self.is_alive:
            self.animation_timer += 1
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                # berhenti di frame terakhir, tidak looping
                if self.current_frame < len(self.frames_died) - 1:
                    self.current_frame += 1
            self.image = self.frames_died[int(self.current_frame)]
            self.rect = self.image.get_rect(bottomleft=(self.rect.left, self.ground_y))
            return
        
        
        #kalo lompat
        if self.is_jumping:
            self.vel_y += self.gravity
            self.rect.y += self.vel_y

            if self.vel_y < 0:
                frame_idx = min(
                    int(self.current_frame), len(self.frames_jump_up) - 1
                )
                self.image = self.frames_jump_up[frame_idx]
            else:
                frame_idx = min(
                    int(self.current_frame), len(self.frames_jump_fall) - 1
                )
                self.image = self.frames_jump_fall[frame_idx]

            #kecepatan lompat per frame
            self.current_frame += 0.2

            #mendarat
            if self.rect.bottom >= self.ground_y:
                self.rect.bottom = self.ground_y
                self.vel_y = 0
                self.is_jumping = False
                self.current_frame = 0
        
        #lari
        else:
            self.animation_timer += 1 
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.current_frame = (self.current_frame + 1) % len(
                    self.frames_run
                )
            self.image = self.frames_run[self.current_frame]
            self.rect = self.image.get_rect(bottomleft=(self.rect.left, self.ground_y))

        

    def draw(self,screen):
        screen.blit(self.image, self.rect)
