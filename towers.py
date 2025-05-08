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


            # stop if tower is at max tier
            if tower.tier >= 4:
                return


            # draws the cost of the upgrade
            if get_balance().balance < tower.get_upgrade_cost():
                draw_text("$" + str(tower.get_upgrade_cost()), tower.pos + (0, 35), None, 40, (200, 140, 120))
            else:
                draw_text("$" + str(tower.get_upgrade_cost()), tower.pos + (0, 35), None, 40, (100, 240, 120))

            draw_text("Upgrade: ", tower.pos + (0, 25), None, 40, (200, 200, 40))

    
    def draw_projectiles(self) -> None:
        """
        Draws all projectiles.

        :return: Returns nothing.
        """

        for tower in self:
            tower.projectiles.draw(get_window())

            for projectile in tower.projectiles:
                projectile.update()