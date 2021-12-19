class GameStats:
    """ For checking the stats of the game. """

    def __init__(self,ai):
        """Making the attributes."""
        self.setting = ai.setting
        self.reset_stats()

        # Active or inactive status of the ship....
        self.game_active = True

    def reset_stats(self):
        """For reseting new game. """
        self.ship_left = self.setting.ship_limit