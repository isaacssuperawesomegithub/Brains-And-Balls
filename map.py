import pygame
from towers import Towers
from track import Track
from enemy import Enemy
from utils import *





class Map:
    def __init__(self, map_id):
        self.towers = Towers()
        
        
        # edit these when we have the maps made
        match map_id: 
            case 0:
                self.track = Track([])
            case 1:
                self.track = Track([])
            case 2:
                self.track = Track([])


    def add_enemy(self, enemy: Enemy) -> None:
        """
        Add an enemy to the track.

        :param enemy: Enemy to add to the track.
        :return: Returns nothing.
        """

        self.track.add_enemy(enemy)


    def draw_towers(self) -> None:
        """
        Draws towers.

        :return: Returns nothing.
        """
        self.towers.draw_towers()
    