import pygame
from utils import *

class Towers(pygame.sprite.Group):
    def __init__(self):
        super().__init__()


    def draw(self):
        for sprite in self:
            sprite.draw()


    # draw each tower in the list
    def draw_range(self) -> None:
        """
        Draws the range of tower if hovering with cursor.

        :return: Returns nothing.
        """

        window = get_window()

        for tower in self:
            if tower.get_distance_from(get_mouse_pos()) > tower.size:
                continue

            tower_range = tower.get_range()
            tower_pos = tower.get_pos()

            surf = pygame.Surface((tower_range * 2, tower_range * 2), pygame.SRCALPHA) # create a surface that can be transparent
            pygame.draw.circle(surf, (100, 100, 100, 150), (tower_range, tower_range), tower_range) # draw a circle centered on the tower
            
            window.blit(surf, (tower_pos[0] - tower_range, tower_pos[1] - tower_range)) # blit the circle
            window.blit(tower.image, tower.rect) # reblit the tower (so it shows in front of the circle)

    
    def draw_projectiles(self) -> None:
        """
        Draws all projectiles.

        :return: Returns nothing.
        """

        for tower in self:
            tower.projectiles.draw(get_window())

            for projectile in tower.projectiles:
                projectile.update()