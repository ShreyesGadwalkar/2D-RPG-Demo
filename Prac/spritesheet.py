import pygame

class SpriteSheet:
    def __init__(self, filename):
        self.filename = filename
        self.sheet = pygame.image.load(filename).convert_alpha()
    
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        return sprite