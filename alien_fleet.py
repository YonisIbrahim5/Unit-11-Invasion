"""
AlienFleet module.

This module creates the Alien Fleet and customizes the layout and movement.
"""
import pygame
from settings import Settings
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """
    Manage the alien fleet: creation, drawing, movement, and collision logic.
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initializes the AlienFleet.

        Args:
            game (AlienInvasion): Main game.
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """
        Creates a fleet of aliens in a cross formation.
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_h = self.settings.screen_h
        screen_w = self.settings.screen_w

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        self._create_cross_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)
    
    def _create_cross_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """
        Create fleet in a cross pattern.

        Args:
            alien_w (int): Width of alien.
            alien_h (int): Height of alien.
            fleet_w (int): Number of aliens width.
            fleet_h (int): Number of aliens width.
            x_offset (int): X offset.
            y_offset (int): Y offset.
        """
        center_col = fleet_w // 2
        center_row = fleet_h // 2

        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset

                if row == center_row or col == center_col:
                    self._create_alien(current_x, current_y)
        

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 ==0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """
        Calculates x and y offsets to the center.

        Args:
            alien_w (int): Width of alien.
            alien_h (int): Height of alien.
            screen_w (int): Width of the screen.
            fleet_w (int): Number of aliens width.
            fleet_h (int): Number of aliens width.
        
        Returns:
            tuple: (x_offset, y_offset)
        """
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space)//2)
        y_offset = int((half_screen - fleet_vertical_space)//2)
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """
        Calculate the number of aliens that fit horizontally and vertically.

        Args:
            alien_w (int): Width of alien.
            screen_w (int): Width of the screen.
            alien_h (int): Height of alien.
            screen_h (int): Height of the screen.

        Returns:
            tuple: (fleet_w, fleet_h)
        """
        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h/2)//alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2
        
        if fleet_h == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2
        
        
        return int(fleet_w), int(fleet_h)

        
    def _create_alien(self, current_x: int, current_y: int):
        """"
        Creates an alien and adds it to the fleet.

        Args:
            current_x (int): X.
            current_y (int): Y.
        """
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    
    def _check_fleet_edges(self):
        """
        Checks if any aliens hit the screen edges and reverse the direction.
        """
        alien : Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """
        Moves the fleet down.
        """
        for alien in self.fleet:

            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        """
        Update the fleets position and direction.
        """
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """
        Draws all aliens on the screen.
        """
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        alien : Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self):
        """
        Check whether the fleet has been completely destroyed.

        Returns:
            bool: True if no aliens are left.
        """
        return not self.fleet

