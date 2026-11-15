import json
import pygame

#ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# MINIMIZE_WIDTH = SCREEN_WIDTH * 2 // 3
# MINIMIZE_HEIGHT = SCREEN_HEIGHT * 2 // 3

FPS = 60

TITLE = "SobiRun"
TITLE_SCREEN = "assets/images/titlemenu.png"



def load_sound(sound_id, volume=1.0):
    try:
        with open("assets/assets.json","r") as f:
            sound = json.load(f)

        sound_path = None
        for item in sound:
            if item.get("id") == sound_id:
                sound_path = item.get("path")
                break

        if not sound_path:
            print(f"Gagal membuat: Sound dengan ID '{sound_id}' tidak ditemukan di asset.json")
            return None
        
        snd= pygame.mixer.Sound(sound_path)
        snd.set_volume(volume)
        return snd
        
    except Exception as e:
        print(f"gagal memuat {e}")
        return None