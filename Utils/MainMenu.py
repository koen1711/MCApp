import pygame_gui
import pygame
from pygame_gui.core import ObjectID

class MainMenu:
    def __init__(self, manager, ws):
        self.window_surface = ws
        self.manager = manager
        self.play_btn = None
        self.setup_btns(manager)
    
    def setup_btns(self, manager):
        # width ratio: 800/300 = 2.6666666666666665
        # height ratio: 600/50 = 12
        x, y = self.window_surface.get_size()
        self.play_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x/2 - ((x/2.6666666666666665)/2), y/2 - ((y/12)/2)), ((x/2.6666666666666665, y/12))),text='Play',manager=manager,
        object_id=ObjectID(class_id='@play_btn',
        object_id='@play_btn'))
    def resize(self, btn, x, y, oldwinx, oldwiny):
        rectx = btn.relative_rect.width
        recty = btn.relative_rect.height
        # calculate the new position of the button
        newx = (btn.relative_rect.x / oldwinx) * x
        newy = (btn.relative_rect.y / oldwiny) * y
        # calculate the new size of the button
        newrectx = (rectx / oldwinx) * x
        newrecty = (recty / oldwiny) * y
        # set the new position and size of the button
        btn.set_dimensions((newrectx, newrecty))
        btn.set_position((newx, newy))
        
        
        

