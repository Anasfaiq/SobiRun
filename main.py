import pygame
import sys
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE
from src.ui import UI
from src.states.score_manager import ScoreManager
from src.character.background import Background
from src.character.dino import Sobi


def main():
    #initialisasi pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption(TITLE)

    #inisialisasi main menu 
    menu = UI()
    score_mgr = ScoreManager()
    background = Background()
    char = Sobi()

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

            if event.type == pygame.KEYDOWN:
                if game_state == "MENU" and event.key == pygame.K_SPACE:
                    score_mgr.reset_score()
                    cbar = Sobi()
                    game_state = "PLAYING"
                elif game_state == "PLAYING":
                    if event.key in (pygame.K_SPACE, pygame.K_UP):
                        char.jump()
                    elif event.key == pygame.K_g:
                        score_mgr.on_game_over()
                        game_state = "GAME_OVER"
                elif game_state == "GAME_OVER" and event.key == pygame.K_r:
                    score_mgr.reset_score()
                    char = Sobi()
                    game_state = "PLAYING"
 

        if game_state == "PLAYING":
            #skor bertambah otomatis seiring waktu berjalan 
            background.update()
            score_mgr.update()
            char.update()

        screen.fill((0, 0, 0))

        #render tampilan sesuai game_state
        if game_state == "MENU":
            menu.main_menu(screen)
        elif game_state == "PLAYING":
            background.draw(screen)
            menu.draw_score(screen, score_mgr.get_score_int(), score_mgr.get_high_score_int())
            # render karakter sama obstacle disini 
            char.draw(screen)

        elif game_state == "GAME_OVER":
            menu.game_over(screen, score_mgr.get_score_int, score_mgr.get_high_score_int())

            # elif game_state == "GAME_OVER":
            #     is_correct = ui.handle_input(event)
            #     if is_correct:
            #         score_mgr.reset_score()
            #         game_state = "PLAYING"

            # #ngambil skor untuk di tampilkan screen
            # current_score = score_mgr.get_score_int()
            # high_score = score_mgr.get_high_score_int()

        pygame.display.flip()
        clock.tick(FPS) 

    pygame.quit()
    sys.exit(   )

if __name__ == "__main__":
    main()