"""
Contains the code for the `Game` class, which holds the game's data.
"""

class Game:
    """
    Class to hold information about the state of the game. This include tower positions, wave, enemies, etc.
    """
    def __init__(self):
        self.wave = 1
        self.cash = 500
        self.lives = 20
        self.towers = []
        self.map = 1
