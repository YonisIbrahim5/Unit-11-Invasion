import pygame
from typing import TYPE_CHECKING
from settings import Settings
from arsenal import Arsenal

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()


        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_file_w, self.settings.ship_file_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.arsenal = arsenal

    def update(self):
        # updating the position of the ship
        self._update_ship_arsenal()
        self.arsenal.update_arsenal()

    def _update_ship_arsenal(self):
        temp_speed = self.settings.ship_speed
        
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed
        if self.moving_up and self.rect.top < self.boundaries.top:
            self.x -= temp_speed
        if self.moving_down and self.rect.bottom > self.boundaries.bottom:
            self.x += temp_speed
        
        self.rect.x = self.x
        self.rect.y = self.y
        self._rotate_ship()

    def _rotate_ship(self):

        angle = 0

        if self.moving_up:
            angle = 270
        elif self.moving_down:
            angle = 90
        elif self.moving_left:
            angle = 180
        elif self.moving_right:
            angle = 0
        
        self.image = pygame.transform.rotate(self.image, angle)

     
    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()