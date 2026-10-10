import pygame
import sys
from random import randint
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE
from src.ui import UI
from src.states.score_manager import ScoreManager
from src.character.background import Background
from src.character.dino import Sobi
from src.character.obstacle import Obstacles
from src.character.text_box import TextBox


def main():
    #initialisasi pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SCALED | pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    pygame.display.set_caption(TITLE)

    #inisialisasi main menu 
    menu = UI()
    score_mgr = ScoreManager()
    background = Background()
    char = Sobi()
    # textbox = TextBox("q")
    # obstacle = Obstacles()

    # game speed
    SCALE_X = SCREEN_WIDTH / 1920
    BASE_SPEED = 15 * SCALE_X
    MAX_SPEED = 100 * SCALE_X
    SPEED_STEP = 20 * SCALE_X
    BG_RATIO = 2 / 15
    game_speed = BASE_SPEED

    SLOW_ANIM = 5
    FAST_ANIM = 2


    #state game menu, playing
    game_state = "MENU"

    quit_after_death = False
    
    obstacles = []

    spawn_obstacle = pygame.USEREVENT + 1

    # posisi mouse
    mouse_pos = pygame.mouse.get_pos()

    #deklarasi variabel
    running = True 
    # is_fullscreen = True
    pygame.time.set_timer(spawn_obstacle, randint(1200, 3000))
    #game Looping
    while running :
        #ketika menjalan kan gamenya 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == spawn_obstacle and game_state == "PLAYING":
                obstacles.append(Obstacles())
                pygame.time.set_timer(spawn_obstacle, randint(1500, 3000))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    # if is_fullscreen:
                    #     screen = pygame.display.set_mode((MINIMIZE_WIDTH, MINIMIZE_HEIGHT), pygame.RESIZABLE)
                    #     is_fullscreen = False
                    # else:
                    pygame.display.toggle_fullscreen()
                elif event.key == pygame.K_ESCAPE:
                    if game_state == "PLAYING" and event.key == pygame.K_ESCAPE:
                        char.die()
                        game_state = "DYING"
                        quit_after_death = True
                    elif game_state in ("MENU", "GAME_OVER","QUESTION"):
                        running = False
                if game_state == "MENU" and event.key == pygame.K_SPACE:
                    score_mgr.reset_score()
                    char = Sobi()
                    game_state = "PLAYING"
                    obstacles.clear()
                elif game_state == "PLAYING":
                    if event.key in (pygame.K_SPACE, pygame.K_UP):
                        char.jump()
                    elif event.key == pygame.K_g:
                        char.die()
                        game_state = "DYING"
                elif game_state == "QUESTION":
                    answer = None
                    if event.key in (pygame.K_a, pygame.K_1):
                        answer = 0
                    elif event.key in (pygame.K_b, pygame.K_2):
                        answer = 1
                    elif event.key in (pygame.K_c, pygame.K_3):
                        answer = 2

                    if answer is not None:
                        if textbox.is_correct(answer):
                            obstacles.clear()
                            game_state = "PLAYING"
                        else:
                            char.die()
                            game_state = "DYING"
                elif game_state == "GAME_OVER" and event.key == pygame.K_r:
                    score_mgr.reset_score()
                    char = Sobi()
                    game_state = "PLAYING"
                    obstacles.clear()
                elif game_state == "GAME_OVER" and event.key == pygame.K_m:
                    score_mgr.reset_score()
                    char = Sobi()
                    game_state = "MENU"
                    obstacles.clear()
 

        if game_state == "PLAYING":
            score = score_mgr.get_score_int()
            game_speed = min(BASE_SPEED + (score // 100) * SPEED_STEP, MAX_SPEED)

            #proses animasi char cepet sesuai dengan score
            progres = (game_speed - BASE_SPEED) / (MAX_SPEED - BASE_SPEED)
            char.set_run_speed(SLOW_ANIM - progres * (SLOW_ANIM - FAST_ANIM))
            #skor bertambah otomatis seiring waktu berjalan 
            background.update(game_speed * BG_RATIO)
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
            
            for obs in obstacles[:]:
                obs.move(game_speed)
                if obs.x < -100:
                    obstacles.remove(obs)
            
            for obs in obstacles:
                obs.draw(screen)
                #tabrakan
                if char.get_hitbox().colliderect(obs.get_hitbox()):
                    textbox = TextBox(f"pertanyaan {randint(1, 50)}")
                    game_state = "QUESTION"
                    break
                    # char.die()
                    # textbox.draw(screen)
                    # score_mgr.on_game_over()
                    # game_state = "DYING"

        elif game_state == "QUESTION":
            background.draw(screen)
            menu.draw_score(screen, score_mgr.get_score_int(), score_mgr.get_high_score_int())
            char.draw(screen)
            for obs in obstacles:
                obs.draw(screen)
            textbox.draw(screen)
                    
        elif game_state == "DYING":
            char.update()
            background.draw(screen)
            menu.draw_score(screen, score_mgr.get_score_int(), score_mgr.get_high_score_int())
            char.draw(screen)
            for obs in obstacles:
                obs.draw(screen)
            if char.death_finished():
                score_mgr.on_game_over()
                if quit_after_death:
                    running = False
                else:
                    game_state = "GAME_OVER"

        elif game_state == "GAME_OVER":
            menu.game_over(screen, score_mgr.get_score_int(), score_mgr.get_high_score_int())

        pygame.display.flip()
        clock.tick(FPS) 

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()