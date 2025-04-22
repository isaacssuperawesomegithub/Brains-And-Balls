"""
Main file containging main game loop.
"""

import pygame
from pygame.locals import *

from loading import *
from game import Game

import pickle

window = pygame.display.set_mode((800, 400))
running = True

game_inst = load_data()

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            save(game_inst)
            quit()