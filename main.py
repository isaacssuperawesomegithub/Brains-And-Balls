"""
Main file containging main game loop.
"""

import pygame
from pygame.locals import *

from loading import *
from enemy import Enemy
from tower import Tower
from map import Map
from utils import *

pygame.init()

window = pygame.Surface((600, 400))

display_info = pygame.display.Info()
display_window = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)

map = Map(0)

enemy = Enemy((-50, 210), 2)

tower = Tower(pygame.Vector2(160, 140), 14, 100, 1, .3)


def main():
    map.draw_sprites()
    map.update()
    map.place_tower(tower)
    for event in events:
        if event.type == pygame.KEYDOWN:
            map.add_enemy(Enemy((-50, 210), 2))


clock = pygame.time.Clock()
running = True

# Main loop
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            quit()
    

    main()

    display_window.blit(pygame.transform.scale(window, display_window.get_size()), (0, 0))

    pygame.display.flip()
    clock.tick(60)
