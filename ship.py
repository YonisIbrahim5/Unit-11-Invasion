"""
Ship module for Alien Invasion.

Player's spaceship and its movement, shooting, collision.
"""
import pygame
from typing import TYPE_CHECKING
from settings import Settings
from arsenal import Arsenal

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:
    """
    Class to for the player's ship.
    """
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """
        Initializes the ship and its position.

        Args:
            game (AlienInvasion): Main game.
            arsenal (Arsenal): Arsenal for firing bullets.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()


        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_file_w, self.settings.ship_file_h)
            )
        
        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        
        self.arsenal = arsenal

    def _center_ship(self):
        """
        Centers the ship on the screen.
        """
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """
        Updates ship position and bullet logic.
        """
        # updating the position of the ship
        self._update_ship_arsenal()
        self.arsenal.update_arsenal()

    def _update_ship_arsenal(self):
        """
        Moves the ship based on screen.
        """
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed
        
        self.rect.x = self.x
     
    def draw(self):
        """
        Draw the ship.
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """
        Fire bullets from the ship.
        """
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        """
        Checks for collisions.
        """
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
    