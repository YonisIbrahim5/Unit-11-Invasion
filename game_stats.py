"""
Game Stats module.

Handles tracking of game stats such as score, high score,
maximum score, level, and the remaining lives.
"""
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """Tracks all stats."""
    
    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize game stats.

        Args:
            game (AlienInvasion): Main Game.
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """
        Load saved high score from file, or initialize and save if none already existed.
        """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()  
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """
        Save the current high score to the JSON file.
        """
        scores = {
            'hi_score' : self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        """
        Reset stats for a new game.
        """
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1
    
    def update(self, collisions):
        """
        Updates score and adjust max/hi scores.

        Args:
            collisions (dict): Alien collisions.
        """
        self._update_scores(collisions)
        self._update_max_score()
        self._update_hi_score()
    
    def _update_scores(self, collisions):
        """
        Increase score based on the number of aliens hit.

        Args:
            collisions (dict): Dictionary mapping bullets to hit aliens.
        """
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f'Basic: {self.score}')

    def _update_max_score(self):
        """
        Updates the maximum score if the current score is more.
        """
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')

    def _update_hi_score(self):
        """
        Updates the high score if the current score is more.
        """
        if self.score > self.hi_score:
            self.hi_score = self.score
        #print(f'Max: {self.max_score}')

    
    def update_level(self):
        """
        Updates to the next level.
        """
        self.level += 1
        #print(self.level)
    


    