import pygame
from utils import *
from tower import Tower

class Towers:
    def __init__(self):
        self.towers = []


    # add a tower to the towers list
    def add(self, tower: Tower) -> None:
        self.towers.append(tower)


    # calculate distance of closest tower
    def get_closest_distance_from(self, pos: tuple[int, int]) -> int:
        distances = []
        for tower in self.towers:
            # distance formula
            distances.append(tower.get_distance_from(pos))

        if len(distances) == 0: return -1
        else: return min(distances)


    # draw each tower in the list
    def draw(self) -> None:
        # draw all towers
        for tower in self.towers:
            tower.draw()

        # show range of tower if cursor is hovering over tower
        for tower in self.towers:
            if tower.get_distance_from(get_mouse_pos()) <= 25:
                window = get_window()

                tower_range = tower.get_range()
                tower_pos = tower.get_pos()

                surf = pygame.Surface((tower_range * 2, tower_range * 2), pygame.SRCALPHA)
                pygame.draw.circle(surf, (100, 100, 100, 150), (tower_range, tower_range), tower_range)
                
                window.blit(surf, (tower_pos[0] - tower_range, tower_pos[1] - tower_range))
                tower.draw()


    def __str__(self):
        return str(self.towers)
    
    def __iter__(self):
        return iter(self.towers)