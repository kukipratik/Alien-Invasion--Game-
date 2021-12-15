from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    """Making the class for the bulleto....."""

    def __init__(self,ai):
        """Making the attributes and linking with Sprite..."""
        
        super().__init__()
        self.screen = ai.screen
        self.setting = ai.setting
        
        # linking with bullet attributes.....
        self.bullet_speed = self.setting.bullet_speed
        self.bullet_height = self.setting.bullet_height
        self.bullet_width = self.setting.bullet_width
        self.bullet_color = self.setting.bullet_color

        # Making the scratch for the bullet...
        self.complete_bullet = pygame.Rect(0,0,self.bullet_width,self.bullet_height)

        # Making it's position linked with the ship...
        self.complete_bullet.midtop = ai.ship.ship_shape.midtop

        # Making it's y-coordinate float...
        self.complete_bullet.y = float(self.complete_bullet.y)

    def update(self):
# Note: this function name should be 'update'....
#    --> Because while using the sprite.GROUP() it takes only function named 'update'...
        """Moving the bullet up...."""
        self.complete_bullet.y -= self.bullet_speed

    def draw_bullet(self):
        """For making the bullet..."""
        pygame.draw.rect(self.screen,self.bullet_color,self.complete_bullet)