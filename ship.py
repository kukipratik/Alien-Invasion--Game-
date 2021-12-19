import pygame

class Ship:
    """A class for the description of a ship."""

    def __init__(self,ai):
        """Making attributes."""

        # For screen----------
        self.screen = ai.screen                    # for sharing same screen...
        self.screen_shape = self.screen.get_rect() # considers the screen to be rectangle shape...

        # For ship----------
        self.ship_img = pygame.image.load('Images/rocket.bmp')  # loding the ship image...
        self.rect = self.ship_img.get_rect()              # considers the ship to be rectangle shape...
        self.rect.x = float(self.rect.x)
        self.ship_speed = ai.setting.ship_speed

        # for keeping the ship in specific position------
        self.rect.midbottom = self.screen_shape.midbottom # sets the ship in midbottom position...

        # flag for the continuous movement of the ship.......
        self.right_movement_flag = False
        self.left_movement_flag = False
    
    def update_ship(self):
        """For the continuous movement of ship..."""

        if self.right_movement_flag and self.rect.right < self.screen_shape.right :
            self.rect.x += self.ship_speed
        
        elif self.left_movement_flag and self.rect.left > self.screen_shape.left :
            self.rect.x -= self.ship_speed

    def blitme(self):
        """Draw the ship at its give location."""
        self.screen.blit(self.ship_img,self.rect)

    def center_ship(self):
        """For placing the ship in the center(mid bottom)..."""
        self.rect.midbottom = self.screen_shape.midbottom