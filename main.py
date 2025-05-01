"""
Main file containging main game loop.
"""

import pygame
import random
from pygame.locals import *

from balance import Balance
from map import Map
from loading import *
from tower import *
from enemy import *
from utils import *
from button import *

pygame.init()

# create the window to draw on
window = pygame.Surface((700, 400))

# get screen dimensions
display_info = pygame.display.Info()

# create window scaled to fullscreen
display_window = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)

surf = pygame.surface.Surface((100,400))
surf.fill((188, 91, 19))
rect = surf.get_rect()
rect.topleft = (600,0)

time = 0

map = Map(0)

balance = Balance(100)

font = pygame.Font(size=30)

b1 = Button((35, 35), (650,50), (182, 200, 1), pygame.image.load(r"art/base-zombie.png"))
b2 = Button((35, 35), (650,125), (182, 200, 1), pygame.image.load(r"art/icecream-zombie.png"))
b3 = Button((35, 35), (650,200), (182, 200, 1), pygame.image.load(r"art/bloody-zombie.png"))
towers = [Tower1, Tower2, Tower3]
selected_tower = Tower1

def main():
    global selected_tower
    map.draw_sprites()
    map.update()
    map.place_tower(selected_tower())
    if time % 60 == 0:
        map.add_enemy(random.choice((Enemy1(), Enemy2(), Enemy3())))
    for event in events:
        if event.type == KEYDOWN and 51 >= event.key >= 49:
            selected_tower = towers[event.key - 49]
    
    window.blit(font.render(str(balance), False, (230, 230, 230)), (10, 10))



clock = pygame.time.Clock()
running = True

# Main loop
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            quit()
    

    main()
    window.blit(surf, rect)
    b1.draw_img(window)
    b2.draw_img(window)
    b3.draw_img(window)
    # scale the unscaled window and blit to scaled window
    display_window.blit(pygame.transform.scale(window, display_window.get_size()), (0, 0))
    
    if b1.is_clicked():
        selected_tower = Tower1
    if b2.is_clicked():
        selected_tower = Tower2
    if b3.is_clicked():
        selected_tower = Tower3
    pygame.display.flip()
   
    clock.tick(60)
    time += 1