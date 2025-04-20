from pathlib import Path

class Settings:
    
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'spaceBG.jpg'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'PurpleShip.png'
        self.ship_file_w = 40
        self.ship_file_h = 60
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'blueLaser.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'scifiLaser.mp3'
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        
