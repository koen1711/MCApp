import pygame_gui
import pygame
from pygame_gui.core import ObjectID

# ['UIButton', 'UIDropDownMenu', 'UIHorizontalScrollBar', 'UIHorizontalSlider', 'UIImage', 'UILabel', 'UIPanel', 'UIProgressBar', 'UIScreenSpaceHealthBar', 'UIScrollingContainer', 'UISelectionList', 'UIStatusBar', 'UITextBox', 'UITextEntryLine', 'UITooltip', 'UIVerticalScrollBar', 'UIWindow', 'UIWorldSpaceHealthBar', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'ui_button', 'ui_drop_down_menu', 'ui_horizontal_scroll_bar', 'ui_horizontal_slider', 'ui_image', 'ui_label', 'ui_panel', 'ui_progress_bar', 'ui_screen_space_health_bar', 'ui_scrolling_container', 'ui_selection_list', 'ui_status_bar', 'ui_text_box', 'ui_text_entry_line', 'ui_tool_tip', 'ui_vertical_scroll_bar', 'ui_window', 'ui_world_space_health_bar']


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

class GameUI:
    def __init__(self, manager, ws):
        self.window_surface = ws
        self.manager = manager
        self.reverse_btn = None
        self.engine_status_text = None
        self.lap_counter = None
        self.setup_btns(manager)

    def setup_btns(self, manager):
        # width ratio: 800/100 = 2.6666666666666665
        # height ratio: 600/30 = 20
        # calculate the position of the button

        x, y = self.window_surface.get_size()
        # calculate the size of the button
        rectx = x/8
        recty = y/12

        textrectx = x/4
        textrecty = y/12
        
        lap_counterx = x/2
        lap_countery = y/40

        reverse_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(x/2 - ((x/2.6666666666666665)/2), ((y/30)/2), rectx, recty),text='Reverse',manager=manager,
        object_id=ObjectID(class_id='@reverse_btn',
        object_id='@reverse_btn'))
        engine_status_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x/1.5 - ((x/2.6666666666666665)/2), ((y/30)/2), textrectx, textrecty),text='Engine Status: Forward',manager=manager,
        object_id=ObjectID(class_id='@engine_status_text',
        object_id='@engine_status_text'))
        self.reverse_btn = reverse_btn
        self.engine_status_text = engine_status_text

        lap_counter = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x/2 - ((x/0.75)/2), ((y/0.6)/2), lap_counterx, lap_countery),text='Lap: 1/3',manager=manager,
        object_id=ObjectID(class_id='@lap_counter',
        object_id='@lap_counter'))
        self.lap_counter = lap_counter
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
    def change_engine_status(self, text):
        self.engine_status_text.set_text(text)
    def update_lap_text(self, text):
        self.lap_counter.set_text(f"Laps: {text}")

class LoadingScreen:
    def __init__(self, manager, ws):
        self.window_surface = ws
        self.manager = manager
        self.uiwindow = None
        self.setup_screen(manager)
    def setup_screen(self, manager):
        uiwindow = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((0, 0), (self.window_surface.get_size())),image_surface=pygame.image.load('loadingscreen.jpg'),manager=manager,
        object_id=ObjectID(class_id='@uiwindow',
        object_id='@uiwindow'))
        self.uiwindow = uiwindow
    def resize(self, btn, x, y, oldwinx, oldwiny):
        print(btn.__class__)
        if btn.__class__ == pygame_gui.elements.UIWindow:
            print(btn)
            rectx = btn.rect.width
            recty = btn.rect.height
            # calculate the new position of the button
            newx = (btn.rect.x / oldwinx) * x
            newy = (btn.rect.y / oldwiny) * y
            # calculate the new size of the button
            newrectx = (rectx / oldwinx) * x
            newrecty = (recty / oldwiny) * y
            # set the new position and size of the button
            pygame_gui.elements.UIWindow.set_dimensions(btn, (newrectx, newrecty))
            pygame_gui.elements.UIWindow.set_position(btn, (newx, newy))

        
        
        
class Time:
    def __init__(self, manager, ws):
        self.window_surface = ws
        self.manager = manager
        self.timer_text = None
        self.time = 0
        self.setup_time(manager)
    def setup_time(self, manager):
        x, y = self.window_surface.get_size()
        time_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((x/2 - ((x/2.6666666666666665)/2), y/2 - ((y/12)/2)), ((x/2.6666666666666665, y/12))),text='Time: 0',manager=manager,
        object_id=ObjectID(class_id='@time_text',
        object_id='@time_text'))
        self.timer_text = time_text
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
    def change_time(self, time):
        self.time += time
        self.timer_text.set_text(f'Time: {self.time}')
