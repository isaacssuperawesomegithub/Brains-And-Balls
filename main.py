import pygame
from pygame.locals import *

import pickle

window = pygame.display.set_mode((800, 1200))
running = True

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

def save(game_obj) -> None: 
    """
    Saves the instance of the `Game` class to a .pk1 file in order to easily deserialize object date.

    :param game_obj: The object instance of the `Game` class
    :return: Returns nothing
    """
    with open("save.pkl", 'wb') as file: # Opens/makes a file named `save.pkl` and writes the data of the `Game` instance to it.
        pickle.dump(game_obj, file)

def load() -> Game:
    """
    Opens the `save.pkl` file if it can be found, converts the data, and puts it into an instance of the `Game` class.

    :return: Returns an instance of the `Game` class with loaded save data.
    """
    # Attempts to open a `save.pkl`, or skips if it isn't found
    try:
        with open("save.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return Game()
        

game_inst = load()

print(game_inst.__doc__)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            save(game_inst)
            quit()