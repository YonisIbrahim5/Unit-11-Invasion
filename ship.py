import pygame
from settings import Settings

class Ship:
    from alien_invasion import AlienInvasion
    
    def __init__(self, game: AlienInvasion):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()


        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.screen_w, self.settings.screen_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        self.screen.blit(self.image, self.rect)
