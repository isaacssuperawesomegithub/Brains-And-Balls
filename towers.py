import pygame
from utils import *

class Towers(pygame.sprite.Group):
    def __init__(self):
        super().__init__()


    # draw each tower in the list
    def draw_towers(self) -> None:
        """
        Draws each tower.

        :return: Returns nothing.
        """


        window = get_window()

        # draw all towers
        self.draw(window)

        # show range of tower if cursor is hovering over tower
        for tower in self:
            if tower.get_distance_from(get_mouse_pos()) > tower.size:
                continue

            tower_range = tower.get_range()
            tower_pos = tower.get_pos()

            surf = pygame.Surface((tower_range * 2, tower_range * 2), pygame.SRCALPHA) # create a surface that can be transparent
            pygame.draw.circle(surf, (100, 100, 100, 150), (tower_range, tower_range), tower_range) # draw a circle centered on the tower
            
            window.blit(surf, (tower_pos[0] - tower_range, tower_pos[1] - tower_range)) # draw the circle
            window.blit(tower.image, tower.rect) # draw the tower (so it shows in front of the circle)