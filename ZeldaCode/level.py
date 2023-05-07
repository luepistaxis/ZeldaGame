import pygame

class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        
        #sprite Group Setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
    def run(self):
        pass