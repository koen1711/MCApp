from os import kill
from turtle import back
import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton
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

screen_mask = pygame.mask.from_threshold(window_surface,(255,255,255),(1,1,1))


while is_running:
    time_delta = clock.tick(60)/1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        

        # if play_btn is clicked, then start the game
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == play_btn:
                curgame = Game(pygame, pygame_gui, all_sprites_list, background, manager, play_btn, window_surface)
                background = curgame.bg
                # create track
                track = Track(pygame, background, curgame.player, background)
                curgame.track = track
            if event.ui_element == back_btn:
                play_btn = curgame.end_game()
                curgame = None
                background = pygame.transform.scale(pygame.image.load("background.png"), (x, y))
                play_btn.kill()
                mm.play_btn.kill()
                mm = MainMenu(manager, window_surface)
                play_btn = mm.play_btn
                

        manager.process_events(event)

    window_surface.blit(background, (0, 0))
    manager.update(time_delta)
    all_sprites_list.update()
    all_sprites_list.draw(window_surface)
    x = window_surface.get_width()
    y = window_surface.get_height()
    if x != curwindowx or y != curwindowy:
        manager.set_window_resolution((x, y))
        background = pygame.transform.scale(background, (x, y))
        window_surface = pygame.display.set_mode((x, y), pygame.RESIZABLE)
        
        mm.resize(play_btn, x, y, curwindowx, curwindowy)
        mm.resize(back_btn, x, y, curwindowx, curwindowy)
        curwindowx = x
        curwindowy = y

    if curgame is not None:
        x1 = curgame.player.rect.x
        y1 = curgame.player.rect.y
        if screen_mask.overlap(curgame.player.mask,(curgame.player.rect.x,curgame.player.rect.y)):
            play_btn = curgame.end_game()
            curgame = None
            is_running = False
        if curgame is not None:
            curgame.handle_event(pygame.key.get_pressed())
            if curgame.game_ended:
                play_btn = curgame.play_btn
                background = curgame.bg
                curgame = None
    manager.draw_ui(window_surface)

    pygame.display.update()