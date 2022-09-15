from .Menus import *
from .GameClass import * 
import pygame


class Handler:
    def __init__(self):
        self.hit_last_time = False
    def EventHandler(self, pygame_gui, event, curgame, play_btn, back_btn, reverse_btn, text, gameui, loading_screen, x, y, window_surface, background, manager, all_sprites_list, is_running):
        
        if event.type == pygame.QUIT:
                is_running = False
            

        # if play_btn is clicked, then start the game
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == play_btn:
                loading_screen = LoadingScreen(manager, window_surface)
                window = loading_screen.uiwindow
                curgame = Game(pygame, pygame_gui, all_sprites_list, background, manager, play_btn, window_surface, 1)
                background = curgame.bg
                # create track
                


                gameui  = GameUI(manager, window_surface)
                text = gameui.engine_status_text
                reverse_btn = gameui.reverse_btn
                
            if event.ui_element == back_btn:
                play_btn = curgame.end_game()
                curgame = None
                background = pygame.transform.scale(pygame.image.load("background.png"), (x, y))
                play_btn.kill()
                mm.play_btn.kill()
                mm = MainMenu(manager, window_surface)
                play_btn = mm.play_btn
                reverse_btn.kill()
                text.kill()
                gameui.engine_status_text.kill()
                gameui.reverse_btn.kill()
                gameui = None
                text = None
                reverse_btn = None
            if event.ui_element == reverse_btn:
                if gameui is not None:
                    curgame.player.reverse()
                    if curgame.player.reversing:
                        text = gameui.change_engine_status("Engine Status: Reversing")
                        reverse_btn = gameui.reverse_btn
                        text = gameui.engine_status_text
                    else:

                        text = gameui.change_engine_status("Engine Status: Forward")
                        reverse_btn = gameui.reverse_btn
                        text = gameui.engine_status_text

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print(pygame.mouse.get_pos())
            
                
        if curgame is not None:
            if curgame.player is not None:
                v = curgame.player.check_hit_finish(curgame.track.start_finish)
                if v == True:
                    if self.hit_last_time == False:
                        curgame.laps_increase()
                        self.hit_last_time = True
                else:
                    self.hit_last_time = False
                gameui.update_lap_text(curgame.laps)
        manager.process_events(event)
        return curgame, play_btn, back_btn, reverse_btn, text, gameui, loading_screen, background, manager, all_sprites_list, is_running