"""
Main file containging main game loop.
"""

import pygame
from pygame.locals import *

from loading import *
from game import Game
from enemy import Enemy
from tower import Tower
from map import Map
from utils import *

window = pygame.display.set_mode((600, 400))

map = Map(0)

enemy = Enemy((-50, 210), 2)

tower = Tower(pygame.Vector2(160, 140), 14, 100, 1, .3)


def main():
    map.draw_sprites()
    map.update()
    map.place_tower(tower)
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            map.add_enemy(Enemy((-50, 210), 2))



clock = pygame.time.Clock()
running = True

# Main loop
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            quit()
    
    window.fill((0, 0, 0))
    main()

    pygame.display.flip()
    clock.tick(60)
