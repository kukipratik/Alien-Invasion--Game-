import sys
import pygame

from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Class for game to manage it's behaviours."""

    def __init__(self):
        """Making the attributes and instances..."""

        # linking the pygame attributes........
        pygame.init()
        pygame.display.set_caption('Alien Invasion.')

        # setting the screen and it's size-------
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        # Making the instance of the setting,ship,bullet(in group)......
        self.setting = Setting()        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_alien_fleet() 

    def run_game(self):
        """For running the game."""

        while 1:
            """For the smooth movement of the screen."""
            """This loop keeps running even if u don't do anything"""
            
            self._check_events()
            self.ship.update_ship()
            self.bullets.update()   # Pay attention while using this method hai...
            self._update_bullet()
            self._update_alien()
            self._update_screen()

    # Helping methods.............
    def _create_alien_fleet(self):
        """for creating the aliens...."""
        '''Spacing between any two alien = width of 1 alien...'''

        # creating an alien and finding no. of aliens in a row.....
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        ship_height = self.ship.ship_shape.height

        # for finding the no. of aliens in a row....
        free_space_x = self.screen_width - (2*alien_width)
        no_of_aliens_x = free_space_x // (2*alien_width)

        # for finding the no. of aliens in a column....
        free_space_y = self.screen_height - (3*alien_height) - ship_height
        no_of_aliens_y = free_space_y // (2*alien_height)

        '''// = returns int value(without remainder)'''

        for alien_number_y in range(no_of_aliens_y):
            """ For inserting new column """
            for alien_number_x in range(no_of_aliens_x):
                """ For inserting alien in a row """
                self._create_alien(alien_number_x,alien_number_y)

    def _create_alien(self,alien_number_x,alien_number_y):
        """for adding the alien created..."""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        alien.x = alien_width + 2*alien_width*alien_number_x
        alien.rect.x = alien.x

        alien.y =  2*alien_height*alien_number_y
        alien.rect.y = alien.y

        self.aliens.add(alien)

    def _check_events(self):
        """for responding the events."""
        
        for event in pygame.event.get():
            """Analizing the events from the user."""
            
            # When player wants to terminate the game-------
            if event.type == pygame.QUIT:
                sys.exit()
            
            # when player presses the key---------
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            # When player releases the key--------
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Responds to the pressing the keys..."""

        if event.key == pygame.K_RIGHT:
            self.ship.right_movement_flag = True
            
        elif event.key == pygame.K_LEFT:
            self.ship.left_movement_flag = True
        
        elif event.key == pygame.K_q :
            sys.exit()
    
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """for making new bullet and adding them in group"""
        if len(self.bullets) < self.setting.max_bullets:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self,event):
        """Responds to the releasing of the keys...."""

        if event.key == pygame.K_RIGHT:
            self.ship.right_movement_flag = False
            
        elif event.key == pygame.K_LEFT:
            self.ship.left_movement_flag = False

    def _update_bullet(self):
        """For removing the excess bullets from the screen."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # for killing the alien with bullet...
        collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

                
    def _update_alien(self):
        """For updating the position of the alien fleet."""
        self._check_fleet_edge()
        self.aliens.update()

    def _check_fleet_edge(self):
        '''Checking hitting of alien with edge...'''
        # .sprites() for making it list maybe....
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_direction()
                break

    def _change_direction(self):
        '''changing the direction of the fleet and droping it down again...'''
        for alien in self.aliens.sprites():
            alien.rect.y =  alien.rect.y + self.setting.alien_speed_y

        self.setting.fleet_direction *= -1

    def _update_screen(self):
        """For redrawing every elements in screen before updating the screen..."""
        
        #for Setting the bg color for every loop............
        self.screen.fill(self.setting.bg_color)

        # for replacing the ship in new position...........
        self.ship.blitme()

        # for drawing every bullets as per their new position......
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # for drawing the alien in the screen....
        self.aliens.draw(self.screen)
        """This draw() method is readymade method in 'sprite.Group' """

# for who is wandering how come 'bullet' have method 'draw_bullet()'; it's because:
#   --> bullet comes from 'group of sprites' and while making that group we used 'new_bullet' to make 'bullet'...
#   which in turn means that 'bullet' is originated from 'new_bullet' i.e. bullet is new_bullet which is instance.

        #for changing the screen motion.......
        pygame.display.flip()

if __name__ == '__main__':
    # Making the instance and running the game......
    ai = AlienInvasion()
    ai.run_game()