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
        self.starting_ship_count = 3

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'blueLaser.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'scifiLaser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'boomSound.mp3'
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'alienSS.png'
        self.fleet_speed = 1
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1
        self.fleet_drop_speed = 40

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen' / 'Silkscreen-Bold.tff'

        
