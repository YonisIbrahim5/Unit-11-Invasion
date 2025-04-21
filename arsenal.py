"""
Arsenal module for Alien Invasion.

This class manages the players ammo.
"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    """
    A class to manage arsenal.
    """
    def __init__(self, game: 'AlienInvasion'):
        """
        Initializes the arsenal.

        Args:
            game (AlienInvasion): Main game.
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """
        Updates the all bullets in the arsenal.
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """
        Remove bullets that have gone off screen.
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """
        Draws all bullets.
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()
    
    def fire_bullet(self):
        """
        Fires a bullet.

        Returns:
            bool: True or false if a bullet was fired.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False