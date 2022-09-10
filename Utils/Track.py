

class Track:
    def __init__(self, pygame, pygame_gui, manager, sur):
        # draw checpoints on the track
        self.pygame = pygame
        self.pygame_gui = pygame_gui
        self.manager = manager



        self.checkpoints = []
        self.checkpoints.append(pygame.Rect(0, 0, 100, 100))
        self.checkpoints.append(pygame.Rect(0, 0, 100, 100))
        self.checkpoints.append(pygame.Rect(0, 0, 100, 100))
        self.checkpoints.append(pygame.Rect(0, 0, 100, 100))
        self.checkpoints.append(pygame.Rect(0, 0, 100, 100))
        self.checkpoints.append(pygame.Rect(0, 0, 100, 100))
        self.checkpoints.append(pygame.Rect(0, 0, 100, 100))
        self.draw(sur)

    def draw(self, sur):
        # draw the track
        # draw the checkpoints
        pygame = self.pygame
        for checkpoint in self.checkpoints:
            pygame.draw.rect(sur, (0, 0, 0), checkpoint)
    def resize(self, sur, x, y, oldwinx, oldwiny):
        pygame = self.pygame
        for checkpoint in self.checkpoints:
            # calculate the new position of the button
            newx = (checkpoint.x / oldwinx) * x
            newy = (checkpoint.y / oldwiny) * y
            # calculate the new size of the button
            newrectx = (checkpoint.width / oldwinx) * x
            newrecty = (checkpoint.height / oldwiny) * y
            # set the new position and size of the button
            checkpoint.width = newrectx
            checkpoint.height = newrecty
            checkpoint.x = newx
            checkpoint.y = newy
        self.draw(sur)	
            