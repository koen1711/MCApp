from .OtherSprites import *

class Track:
    def __init__(self, pygame, pygame_gui, manager, sur, all_sprites_list, bg):
        # draw checpoints on the track
        self.pygame = pygame
        self.pygame_gui = pygame_gui
        self.manager = manager
        self.all_sprites_list = all_sprites_list
        self.background = bg

        self.start_finish = Start_Finish(434, 525, sur.get_width(), sur.get_height(), sur)
        
        # register the start/finish line
        self.all_sprites_list.add(self.start_finish)
        self.all_sprites_list.update()
        self.checkpoints = []
        self.checkpoints.append(Checkpoint(629, 316, 681, 275, 90, sur))
        
        self.draw(sur)

    def draw(self, sur):
        # draw the track
        # draw the checkpoints
        pygame = self.pygame
        for checkpoint in self.checkpoints:
            self.all_sprites_list.add(checkpoint)
            self.all_sprites_list.update()

    def resize(self, sur, x, y, oldwinx, oldwiny):
        pygame = self.pygame
        for checkpoint in self.checkpoints:
            checkpoint.resize()
            self.all_sprites_list.add(checkpoint)
            self.all_sprites_list.update()
        self.start_finish.resize(x, y, oldwinx, oldwiny)
        self.draw(sur)	


            