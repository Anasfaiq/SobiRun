import pygame
import sys
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE
from src.ui import UI
from src.states.score_manager import ScoreManager


def main():
    #initialisasi pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption(TITLE)

    #inisialisasi main menu 
    menu = UI()
    score_mgr = ScoreManager()

    #state game menu, playing
    game_state = "MENU"


    #deklarasi variabel
    running = True 

    #game Looping
    while running :
        #ketika menjalan kan gamenya 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill()

        #render tampilan sesuai game_state
        if game_state == "MENU":
            print("ini buat masukkin clas dari ui")
        elif game_state == "PLAYING":
            if game_state == "PLAYING":
                # Skor nambah terus setiap frame
                score_mgr.update()

            elif game_state == "GAME_OVER":
                is_correct = ui.handle_input(event)
                if is_correct:
                    score_mgr.reset_score()
                    game_state = "PLAYING"

            #ngambil skor untuk di tampilkan screen
            current_score = score_mgr.get_score_int()
            high_score = score_mgr.get_high_score_int()
            
        if game_state == "PLAYING":
            #skor bertambah otomatis seiring waktu berjalan 
            score_mgr.update()

        pygame.display.flip()
        clock.tick(FPS) 

    pygame.quit()
    sys.exit(   )

if __name__ == "__main__":
    main()