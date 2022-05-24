import sys
import pygame
from time import sleep

from pygame import mouse

from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

class AlienInvasion:
    """Class for game to manage it's behaviours."""

    def __init__(self):
        """Making the attributes and instances..."""

        # linking the pygame attributes........
        pygame.init()
        pygame.display.set_caption('Alien Invasion.')

        # setting the screen and it's size-------
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        # Making the instance of the setting,stats,ship,bullet(in group),aliens(in group)......
        self.setting = Setting() 
        self.stats = GameStats(self)       
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_alien_fleet() 

        # for the button.....
        self.play_button = Button(self,'Play')

    '''Note:- The "rect" of any sprite is needed in order to find the collision between using "pygame". '''

    def run_game(self):
        """For running the game."""

        while 1:
            """For the smooth movement of the screen."""
            """This loop keeps running even if u don't do anything"""
            
            self._check_events()

            # if block execute only when game is active....
            if self.stats.game_active:
                self.ship.update_ship()
                # Pay attention while using "self.bullets.update()" method hai...
                self.bullets.update()   
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
        ship_height = self.ship.rect.height

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

            # When Player presses the mouse button......
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button_click(mouse_pos)
    
    def _check_play_button_click(self,mouse_pos):
        """To start new game when player clicks the play button."""
        
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        
        if button_clicked and not self.stats.game_active :
            
            # for Activing the game...
            self.stats.game_active = True

            # for Reseting the game stats and removing the remaining elements...
            self.stats.reset_stats()
            self.aliens.empty()
            self.bullets.empty()

            # for creating new elements....
            self._create_alien_fleet()
            self.ship.center_ship()

            # Making the mouse invisible...
            pygame.mouse.set_visible(False)

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

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        '''for killing the alien with bullet...'''
        collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

        # When all aliens are shot down...
        # Destroying all the bullets and restoring the fleet....
        if not self.aliens:
            self.bullets.empty()
            self._create_alien_fleet()
                
    def _update_alien(self):
        """For updating the position of the alien fleet."""
        self._check_fleet_edge()
        self.aliens.update()

        # When alien reaches the bottom....
        self._check_alien_in_bottom()

        # When the ship hit the alien....
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()

    def _check_alien_in_bottom(self):
        """Consider as ship hit when alien reach the bottom of screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_hit()

    def _ship_hit(self):
        """ When the alien hits the ship. """
        if self.stats.ship_left > 0:
            # Decreasing the no. of ship left....
            self.stats.ship_left -= 1

            # Removing all current aliens and bullets...
            self.aliens.empty()
            self.bullets.empty()

            # Creating new alien fleet and keeping the ship in center again....
            self._create_alien_fleet()
            self.ship.center_ship()

            # Pausing the game for 0.6 sec....
            sleep(0.6)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

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

        # Drawing the play button when game is inactive...
        if not self.stats.game_active:
            self.play_button.draw_button()

        #for changing the screen motion.......
        pygame.display.flip()

if __name__ == '__main__':
    # Making the instance and running the game......
    ai = AlienInvasion()
    ai.run_game()