import pygame
from towers import Towers
from tower import Tower
from track import Track
from enemy import Enemy
from utils import *





class Map(pygame.sprite.Sprite):
    def __init__(self, map_id):
        super().__init__()
        self.towers = Towers()
        
        # edit these when we have the maps made
        match map_id: 
            case 0:
                self.image = pygame.image.load("./art/map1.png")
                self.track = Track([pygame.Vector2(-16, 210), pygame.Vector2(100, 210), pygame.Vector2(100, 95), pygame.Vector2(220, 95), pygame.Vector2(220, 255), pygame.Vector2(380, 255), pygame.Vector2(380, 175), pygame.Vector2(700, 175)])
            case 1:
                raise TypeError("Map doesn't exist.")
                self.image = pygame.image.load("./art/")
                self.track = Track([])
            case 2:
                raise TypeError("Map doesn't exist.")
                self.image = pygame.image.load("./art/")
                self.track = Track([])

        self.rect = self.image.get_rect()

        self.rect.topleft = (0, 0)


    def add_enemy(self, enemy: Enemy) -> None:
        """
        Add an enemy to the track.

        :param enemy: Enemy to add.
        :return: Returns nothing.
        """

        self.track.add(enemy)


    def add_tower(self, tower: Tower) -> None:
        """
        Add a tower to the map
        
        :param tower: Tower to add.
        :return: Returns nothing.
        """

        self.towers.add(tower)


    def draw_enemies(self) -> None:
        """
        Draws enemies.

        :return: Returns nothing.
        """
        
        self.track.draw(get_window())


    def draw_towers(self) -> None:
        """
        Draws towers.

        :return: Returns nothing.
        """

        self.towers.draw(get_window())
        self.towers.draw_range()


    def draw_projectiles(self) -> None:
        """
        Draws projectiles.

        :return: Returns nothing.
        """

        self.towers.draw_projectiles()
    

    def draw_tower_placement(self, tower: Tower) -> None:
        """
        Draws a overlay of where a tower can be placed.

        :param tower: Tower image to display.
        :return: Returns nothing.
        """

        targets = self.track.targets
        overlay_color = (0, 255, 0, 128)

        for idx in range(len(targets) - 1):
            x1, y1 = targets[idx].xy
            x2, y2 = targets[idx + 1].xy
            
            #pygame.draw.rect(get_window(), (255, 0, 0), (min(x1, x2), min(y1, y2), abs(x2 - x1) + 1, abs(y2 - y1) + 1))
            pygame.draw.rect(get_window(), (255, 0, 0), (min(x1, x2), min(y1, y2), abs(x2 - x1) + 1, abs(y2 - y1) + 1))


            if get_distance_from_line(targets[idx], targets[idx + 1], tower.get_pos()) <= tower.get_size():
                overlay_color = (255, 0, 0, 128)
                break


        surf = tower.image
        surf = pygame.transform.scale(surf, (32, 32))

        draw_surf = pygame.Surface(surf.get_size(), pygame.SRCALPHA)

        rect = surf.get_rect()

        rect.center = get_mouse_pos()


        for x in range(surf.get_width()):
            for y in range(surf.get_height()):
                if surf.get_at((x, y)).a != 0:
                    draw_surf.set_at((x, y), overlay_color)


        get_window().blit(draw_surf, rect)


    def update(self) -> None:
        """
        Updates all sprites
        
        :return: Returns nothing.
        """

        # update projectiles
        for tower in self.towers:
            for projectile in tower.projectiles:
                projectile.update()

        # update enemies
        self.track.update()


    def draw(self) -> None:
        """
        Draws the map sprite.

        :return: Returns nothing.
        """

        get_window().blit(self.image, self.rect)