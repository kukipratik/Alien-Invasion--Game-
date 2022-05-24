class Setting:
    """Creating setting class for the 'alien invasion' game."""

    def __init__(self):
        """Making attributes for the game settings."""
        
        # for screen... 
        self.bg_color = (230,230,230)

        # for ship...
        self.ship_limit = 3

        # for bullet...
        self.bullet_color = (60,60,60)
        self.bullet_width = 4
        self.bullet_height = 15
        self.max_bullets = 3

        # for alien fleet....
        self.alien_speed_y = 100

        # Increase speed by......
        self.speed_up_by = 1.1

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """Attributes that will change."""
        self.alien_speed_x = 1
        self.ship_speed = 1.5
        self.bullet_speed = 1.75

        '''For fleet direction:- '''
        # 1 => right direction
        # -1 => left direction
        self.fleet_direction = 1