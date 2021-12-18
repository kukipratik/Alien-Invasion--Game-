import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """For making the fleet of aliens..."""

    def __init__(self,ai_game):
        """Making the attributes and linking with 'Sprite' """

        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        # Getting images and making it's rect...
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()

        # for maintaining the gap between them...
        self.x = self.rect.width
        self.y = self.rect.height

    def update(self):
        """For moving the fleet of the alien."""
        self.x += self.setting.alien_speed_x
        self.rect.x = self.x