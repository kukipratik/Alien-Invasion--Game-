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