from pygame_gui.core import ObjectID
from .CarSprite import Player

class Game:
    def __init__(self, pygame, pygame_gui, all_sprites_list, background, manager, play_btn, window_surface):
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
        self.laptime = 0
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
        player = Player((0, 0, 255), 100, 400, 100, 100, self.background)  # color, x, y, width, height
        self.player = player
        self.all_sprites_list.add(player)
        self.pygame.display.update()

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
            player.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            player.moveRight(5)
        if keys[pygame.K_UP]:
            player.moveUp(5)
        if keys[pygame.K_DOWN]:
            player.moveDown(5)
        if keys[pygame.K_ESCAPE]:
            self.play_btn = self.end_game()
            self.is_running = False
        player.check_out_of_bounds(self, self.window_surface)
    def update_time(self, time):
        self.time += time
    

