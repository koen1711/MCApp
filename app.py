

from types import NoneType
import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from Utils import *

pygame.init()
curwindowx = 800
curwindowy = 600
pygame.display.set_caption('Formula 1')
window_surface = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

background = pygame.Surface((800, 600), pygame.RESIZABLE)
background.fill(pygame.Color('#000000'))

#add background image to the window 
background = pygame.image.load("background.png")

manager = pygame_gui.UIManager((800, 600), 'themes.json')

mm = MainMenu(manager, window_surface)
play_btn = mm.play_btn
back_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 25), (100, 50)),text='Back',manager=manager,
object_id=ObjectID(class_id='@back_btn',
object_id='@back_btn'))

all_sprites_list = pygame.sprite.Group()

clock = pygame.time.Clock()
is_running = True

curgame = None


reverse_btn = None
text = None
gameui = None
loading_screen = None
timer = None
timer_text = None
window = None
cc = ChooseCar(manager, window_surface)
cc.appear()
e = Handler()



while is_running:
    time_delta = clock.tick(60)/1000.0
    window_surface.blit(background, (0, 0))

    for event in pygame.event.get():
        curgame1 = curgame
        x, y = pygame.display.get_surface().get_size()
        curgame, play_btn, back_btn, reverse_btn, text, gameui, loading_screen, background, manager, all_sprites_list, is_running, mm = e.EventHandler(pygame_gui, event, curgame, play_btn, back_btn, reverse_btn, text, gameui, loading_screen, x, y, window_surface, background, manager, all_sprites_list, is_running, mm)
        if curgame is None and curgame1 is not None:
            # kill all sprites
            for sprite in all_sprites_list:
                
                sprite.kill()

            # kill all ui elements
            for element in manager.get_root_container().elements:
                # check if it is not back_btn or play_btns
                if element != back_btn and element != play_btn:
                    element.kill()
            gameui = None
            
            timer_text.kill()
            text = None
            reverse_btn = None
            loading_screen = None
            timer = None
            timer_text = None
                
                
        curgame1 = curgame
    # check if 
    manager, all_sprites_list, window_surface=e.BaseUpdates(manager, time_delta, all_sprites_list, window_surface, curgame)
    
    x = window_surface.get_width()
    y = window_surface.get_height()
    if x != curwindowx or y != curwindowy:
        manager.set_window_resolution((x, y))
        background = pygame.transform.scale(background, (x, y))
        window_surface = pygame.display.set_mode((x, y), pygame.RESIZABLE)
        
        if loading_screen is not None:
            loading_screen.resize(window, x, y, curwindowx, curwindowy)
        if gameui is not None:
            gameui.resize(reverse_btn,x, y, curwindowx, curwindowy)
            gameui.resize(text,x, y, curwindowx, curwindowy)
            curgame.player.resize(x, y, curwindowx, curwindowy)
            curgame.track.resize(window_surface, x, y, curwindowx, curwindowy)
            if timer != None:
                timer.resize(timer.timer_text, x, y, curwindowx, curwindowy)

        else:
            mm.resize(play_btn, x, y, curwindowx, curwindowy)
            mm.resize(back_btn, x, y, curwindowx, curwindowy)
        curwindowx = x
        curwindowy = y
    
    if curgame is not None or not NoneType:
        if curgame.player is not None or not NoneType:
            if loading_screen is not None:
                timer = Time(manager, window_surface)
                timer_text = timer.timer_text
                loading_screen.uiwindow.kill()
                loading_screen = None
            x1 = curgame.player.rect.x
            y1 = curgame.player.rect.y
            try:
                if background.get_at(curgame.player.rect.center) == (0, 0, 0, 255):
                    play_btn = curgame.respawn()
                    
                    #curgame = None
                    #is_running = False
            except:
                pass
            if curgame is not None:
                curgame.handle_event(pygame.key.get_pressed())
                if curgame.game_ended:
                    play_btn = curgame.play_btn
                    background = curgame.bg
                    reverse_btn.kill()
                    text.kill()
                    gameui.reverse_btn.kill()
                    gameui.engine_status_text.kill()
                    curgame = None
                    gameui = None
                    
    manager.draw_ui(window_surface)

    pygame.display.update()
    if timer != None:
        timer.change_time(time_delta)
    