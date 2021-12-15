import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """For making the fleet of aliens..."""

    def __init__(self,ai_game):
        """Making the attributes and linking with 'Sprite' """

        super().__init__()
        self.screen = ai_game.screen

        # Getting images and making it's rect...
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()

        # for maintaining the gap between them...
        self.rect.x = float(self.rect.width)
        self.rect.y = self.rect.height