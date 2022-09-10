import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, color, x, y, width, weight, background):
        super().__init__() 
        self.color = color
        self.bg = background
        self.image = pygame.Surface([width, weight])
        self.image.fill(color)
        #self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_threshold(self.bg,(255,255,255),(1,1,1))
        #if your player is an image, not one colour, then you can do 
        #self.mask = pygame.mask.from_surface(self.image)
    def moveLeft(self, pixels):
        self.rect.x -= pixels
    def moveRight(self, pixels):
        self.rect.x += pixels
    def moveUp(self, pixels):
        self.rect.y -= pixels
    def moveDown(self, pixels):
        self.rect.y += pixels
    def check_out_of_bounds(self, game, pg):
        if self.rect.x < 0:
            game.end_game()
        if self.rect.x > pg.get_width():
            game.end_game()
        if self.rect.y < 0:
            game.end_game()
        if self.rect.y > pg.get_height():
            game.end_game()
    

        