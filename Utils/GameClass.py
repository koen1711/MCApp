from .Track import Track
from threading import Thread
from pygame_gui.core import ObjectID

from .AllCars import number_to_class
from .CarSprite import CarSprite

class Game:
    def __init__(self, pygame, pygame_gui, all_sprites_list, background, manager, play_btn, window_surface, carnumber):
        self.carnumber = carnumber
        self.window_surface = window_surface
        self.pygame_gui = pygame_gui
        self.pygame = pygame
        self.all_sprites_list = all_sprites_list
        self.background = background
        self.manager = manager
        self.play_btn = play_btn
        self.is_running = True
        self.time = 0
        self.track = None
        self.lapsrequired = 3
        self.laps = 0
        self.laptime = []
        self.bestlap = 0
        self.bestlaptime = 0
        self.player = None
        self.game_ended = False
        self.bg = self.pygame.image.load("background.png")
        self.start_game()
    def start_game(self): 
        x, y = self.window_surface.get_size()
        img = self.pygame.transform.scale(self.pygame.image.load("circuit.png"), (x, y))
        self.bg = img
        self.background.blit(img, (0, 0))
        self.play_btn.kill()
        self.track = Track(self.pygame, self.pygame_gui, self.manager, self.window_surface, self.all_sprites_list, self.background)
        def ThreadedFunction2():
            cla = number_to_class(self.carnumber)
            car = self.pygame.image.load("Cars/car" + str(self.carnumber) + ".png")
            player = CarSprite(car, 440, 532, cla, self.background, self.window_surface, 360)  # color, x, y, width, height // 
            
            self.player = player
            self.all_sprites_list.add(player)
            self.pygame.display.update()
        Thread(target=ThreadedFunction2).start()
        

    def end_game(self):
        img = self.pygame.image.load("background.png")
        self.background.blit(img, (0, 0))
        play_btn = self.pygame_gui.elements.UIButton(relative_rect=self.pygame.Rect((250, 275), (300, 50)),text='Play',manager=self.manager,
        object_id=ObjectID(class_id='@play_btn',
        object_id='@play_btn'))
        self.player.kill()
        self.pygame.display.update()
        self.game_ended = True
        self.play_btn = play_btn
        self.bg = img
        return play_btn
    def handle_event(self, keys):
        pygame = self.pygame
        player = self.player
        if keys[pygame.K_LEFT]:
            player.turn("left")
        if keys[pygame.K_RIGHT]:
            player.turn("right")
        if keys[pygame.K_UP]:
            player.accelerate()
        if keys[pygame.K_DOWN]:
            player.brake()
        if keys[pygame.K_SPACE]:
            player.brake()
        if keys[pygame.K_w]:
            player.accelerate()
        if keys[pygame.K_a]:
            player.turn("left")
        if keys[pygame.K_d]:
            player.turn("right")
        if keys[pygame.K_s]:
            player.brake()
        if keys[pygame.K_ESCAPE]:
            self.play_btn = self.end_game()
            self.is_running = False
        player.check_out_of_bounds(self, self.window_surface)
    def update_time(self, time):
        self.time += time
    def laps_increase(self):
        self.laps += 1
        if self.laps == self.lapsrequired:
            self.end_game()
    

