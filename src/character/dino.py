import json 
import pygame

class Sobi:
    def __init__(self, char_id="sobiChar"):
        #load data dari json
        self.data = self.load_data(char_id)

        #memotong gambar sprite
        sprites_info = self.data["sprites"]
        self.frames_run = self.load_sprite_sheet(
            sprites_info["run"]["file"], sprites_info["run"]["frame_count"]
        )
        self.frames_jump_up = self.load_sprite_sheet(
            sprites_info["jump_up"]["file"],
            sprites_info["jump_up"]["frame_count"],
        )
        self.frames_jump_fall = self.load_sprite_sheet(
            sprites_info["jump_fall"]["file"],
            sprites_info["jump_fall"]["frame_count"],
        )

        #animasi
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 5

        #posisi awal
        self.image = self.frames_run[0]
        self.rect = self.image.get_rect(topleft=(50, 280))

        #move / pergerakan
        self.vel_y = 0
        self.jump_power = self.data["jump_power"]
        self.gravity = self.data["gravity"]
        self.ground_y = 200
        self.is_jumping = False

    def load_data(self, char_id):
        with open("assets/assets.json","r") as f:
            characters = json.load(f)
            for char in characters:
                if char["id"] == char_id:
                    return char
        return characters[0]

    def load_sprite_sheet(self, filepath, frame_count):
        sheet = pygame.image.load(filepath).convert_alpha()
        sheet_width = sheet.get_width()
        sheet_height = sheet.get_height()

        frame_width = sheet_width // frame_count
        frames = []

        for i in range(frame_count):
            rect = pygame.Rect(i * frame_width, 0, frame_width, sheet_height)
            frame = sheet.subsurface(rect)
            frames.append(frame)

        return frames

    def jump(self):
        if not self.is_jumping:
            self.vel_y = self.jump_power
            self.is_jumping = True
            self.current_frame = 0

    def update(self):
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
            if self.rect.y >= self.ground_y:
                self.rect.y = self.ground_y
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

    def draw(self,screen):
        screen.blit(self.image, self.rect)
