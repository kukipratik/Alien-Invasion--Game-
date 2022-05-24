import pygame
import pygame.font

class Button:
    """ class for the buttons of the game. """

    def __init__(self,ai,msg):
        """Making attributes."""

        # for screen....
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()

        # for button....
        self.button_width = 200
        self.button_height = 50
        self.button_color = (150,134,119)
        self.text_color = (10,250,20) 
        self.font = pygame.font.SysFont(None,48)
        
        # making scratch(rect) and placing in the centre ...
        self.rect = pygame.Rect(0,0,self.button_width,self.button_height)
        self.rect.center = self.screen_rect.center

        # Preparing for the button msg....
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """Converting msg into rendered img and placing in the center of the button."""

        self.msg_img = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        """Draw the color in button and draw the message in it."""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_img,self.msg_img_rect)