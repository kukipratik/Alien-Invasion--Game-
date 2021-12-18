class Setting:
    """Creating setting class for the 'alien invasion' game."""

    def __init__(self):
        """Making attributes for the game settings."""
        
        # for screen... 
        self.bg_color = (230,230,230)

        # for ship...
        self.ship_speed = 1.5

        # for bullet...
        self.bullet_speed = 1.75
        self.bullet_color = (60,60,60)
        self.bullet_width = 4
        self.bullet_height = 15
        self.max_bullets = 3

        # for alien fleet....
        self.alien_speed_x = 0.7
        self.alien_speed_y = 0.9

        '''For fleet direction:- '''
        # 1 => right direction
        # -1 => left direction
        self.fleet_direction = 1