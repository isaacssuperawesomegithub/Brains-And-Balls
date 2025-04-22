"""
Contains the functions used to save and load the data of the game.
"""

import pickle
from game import Game



def save(game_obj) -> None: 
    """
    Saves the instance of the `Game` class to a .pk1 file in order to easily deserialize object date.

    :param game_obj: The object instance of the `Game` class
    :return: Returns nothing
    """
    with open("save.pkl", 'wb') as file: # Opens/makes a file named `save.pkl` and writes the data of the `Game` instance to it.
        pickle.dump(game_obj, file)

def load_data() -> Game:
    """
    Opens the `save.pkl` file if it can be found, converts the data, and puts it into an instance of the `Game` class.

    :return: Returns an instance of the `Game` class with loaded save data.
    """
    # Attempts to open a `save.pkl` and load data, or create a new instance of `Game` on a first-time use. 
    try:
        with open("save.pkl", "rb") as file:
            print("Data loaded!")
            return pickle.load(file)
    except FileNotFoundError:
        print("File not found, creating new object instance.")
        return Game()

def setup(instance) -> None:
    """
    After data is loaded, setup the game. Load images, set numbers, etc.

    :param instance: The instance of the `Game` class in use.
    :return: Returns nothing.
    """

def main():
    data = load_data()
    setup()
    save

if __name__ == "__main__":
    main()