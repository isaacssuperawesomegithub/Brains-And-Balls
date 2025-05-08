"""
Main file containging main game loop.
"""

import pygame
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
window = pygame.Surface((640, 360))

# get screen dimensions
display_info = pygame.display.Info()

# create window scaled to fullscreen
display_window = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)

surf = pygame.surface.Surface((100,400))
surf.fill((188, 91, 19))
rect = surf.get_rect()
rect.topleft = (540,0)

map = Map(0)

balance = Balance(100000)
health = Health(100)

b1 = Button((35, 35), (560,20), (182, 200, 1), pygame.image.load(r"art/base-zombie.png"), lambda tower: (set_selected_tower(tower)))
b2 = Button((35, 35), (560,60), (182, 200, 1), pygame.image.load(r"art/bloody-zombie.png"), lambda tower: (set_selected_tower(tower)))
b3 = Button((35, 35), (560,100), (182, 200, 1), pygame.image.load(r"art/icecream-zombie.png"), lambda tower: (set_selected_tower(tower)))

towers = [Tower1, Tower2, Tower3]
selected_tower = Tower1

def main():
    for tower in map.towers:
        if tower.rect.collidepoint(get_mouse_pos()) and get_mouse_up():
            tower.upgrade()

    map.draw_sprites()
    map.update()
    map.place_tower(selected_tower())

    for event in events:
        if event.type == KEYDOWN and 51 >= event.key >= 49:
            set_selected_tower(towers[event.key - 49])
    

    draw_text(str(get_balance()), (10, 10), None, 80, (230, 230, 230), "topleft")
    draw_text(str(get_health()), (10, 35), None, 80, (230, 230, 230), "topleft")


def set_selected_tower(tower):
    global selected_tower
    selected_tower = tower


clock = pygame.time.Clock()
running = True

# Main loop
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            quit()
    
    # scale the unscaled window and blit to scaled window
    display_window.blit(pygame.transform.scale(window, display_window.get_size()), (0, 0))
    

    main()
    window.blit(surf, rect)
    b1.draw_img(window)
    b2.draw_img(window)
    b3.draw_img(window)

    b1.update(Tower1)
    b2.update(Tower2)
    b3.update(Tower3)

    pygame.display.flip()
    clock.tick(60)