import pygame
import sys
from random import randint
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, MINIMIZE_WIDTH, MINIMIZE_HEIGHT, FPS, TITLE
from src.ui import UI
from src.states.score_manager import ScoreManager
from src.character.background import Background
from src.character.dino import Sobi
from src.character.obstacle import Obstacles


def main():
    #initialisasi pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    pygame.display.set_caption(TITLE)

    #inisialisasi main menu 
    menu = UI()
    score_mgr = ScoreManager()
    background = Background()
    char = Sobi()
    obstacle = Obstacles()

    #state game menu, playing
    game_state = "MENU"

    
    obstacles = []

    spawn_obstacle = pygame.USEREVENT + 1

    #deklarasi variabel
    running = True 
    is_fullscreen = True

    #game Looping
    while running :
        #ketika menjalan kan gamenya 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == spawn_obstacle:
                obstacles.append(Obstacles())
            pygame.time.set_timer(spawn_obstacle, randint(500, 700))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    if is_fullscreen:
                        screen = pygame.display.set_mode((MINIMIZE_WIDTH, MINIMIZE_HEIGHT), pygame.RESIZABLE)
                    else:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
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
            for obs in obstacles:
                obs.move()
    
                if obs.x < -100:
                    obstacles.remove(obs)
            
            for obs in obstacles:
                obs.draw(screen)
                if char.get_hitbox().colliderect(obs.get_hitbox()):
                    score_mgr.on_game_over()
                    game_state = "GAME_OVER"

        elif game_state == "GAME_OVER":
            menu.game_over(screen, score_mgr.get_score_int(), score_mgr.get_high_score_int())

        pygame.display.flip()
        clock.tick(FPS) 

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()