import pygame
from towers import Towers
from tower import Tower
from track import Track
from wav import Wave
from enemy import *
from utils import *


class Map(pygame.sprite.Sprite):
    def __init__(self, map_id):
        super().__init__()
        self.towers = Towers()
        
        # edit these when we have the maps made
        match map_id: 
            case 0:
                self.image = pygame.image.load("./art/map1.png")
                self.track = Track([pygame.Vector2(-16, 210), pygame.Vector2(100, 210), pygame.Vector2(100, 95), pygame.Vector2(220, 95), pygame.Vector2(220, 255), pygame.Vector2(380, 255), pygame.Vector2(380, 175), pygame.Vector2(616, 175)])
                self.waves = [
                    Wave(Enemy1, 5, 60, self),
                    Wave(Enemy2, 5, 20, self),
                    Wave(Enemy3, 3, 120, self)
                ]

            case 1:
                self.image = pygame.image.load("./art/map2.png")
                self.track = Track([pygame.Vector2(-16, 45), pygame.Vector2(265, 45), pygame.Vector2(265, 370), pygame.Vector2(616, 370)])
                self.waves = [
                    Wave(Enemy1, 5, 60, self),
                    Wave(Enemy2, 5, 20, self),
                    Wave(Enemy3, 3, 120, self)
                ]
                
            case 2:
                raise TypeError("Map doesn't exist.")
                self.image = pygame.image.load("./art/")
                self.track = Track([])

        self.image = pygame.transform.scale(self.image, (600, 400))

        self.current_wave = 0

        self.rect = self.image.get_rect()

        self.rect.topleft = (0, 0)


    def add_enemy(self, enemy: Enemy) -> None:
        """
        Add an enemy to the track.

        :param enemy: Enemy to add.
        :return: Returns nothing.
        """

        enemy.set_pos(list(self.track.targets)[0]) # sets enemy start position
        self.track.add(enemy)


    def add_tower(self, tower: Tower) -> None:
        """
        Add a tower to the map
        
        :param tower: Tower to add.
        :return: Returns nothing.
        """

        tower.set_pos(get_mouse_pos())
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

        self.towers.draw()

        self.towers.draw_range()


    def draw_projectiles(self) -> None:
        """
        Draws projectiles.

        :return: Returns nothing.
        """

        self.towers.draw_projectiles()


    def draw_tower_placement(self, selected_tower: Tower) -> None:
        """
        Draws a overlay of where a tower can be placed.

        :param selected_tower: Tower image to display.
        :return: Returns boolean, True if tower is in a valid position.
        """

        targets = self.track.targets
        valid = get_balance() >= selected_tower.get_cost()

        mouse_pos =  get_mouse_pos()
        tower_size = selected_tower.get_size()


        if valid:
            for idx in range(len(targets) - 1): # invalid if cursor is too close to track
                if get_distance_from_line(targets[idx], targets[idx + 1], mouse_pos) <= tower_size * 2:
                    valid = False
                    break
        
        if valid:
            for other_tower in self.towers: # invalid if cursor is too close to another tower
                if other_tower.get_distance_from(mouse_pos) <= tower_size + other_tower.get_size():
                    valid = False
                    break
        
        if valid:
            if not (tower_size < mouse_pos[0] < self.image.get_width() - tower_size and tower_size < mouse_pos[1] < self.image.get_height() - tower_size):
                valid = False

        
        surf = selected_tower.image

        draw_surf = pygame.Surface(surf.get_size(), pygame.SRCALPHA)

        rect = surf.get_rect()

        rect.center = get_mouse_pos()

        # set the color of the overlay
        if valid: 
            overlay_color = (0, 255, 0, 128)
        else:
            overlay_color = (255, 0, 0, 128)

        # change non-transparent pixels to the overlay color
        for x in range(surf.get_width()):
            for y in range(surf.get_height()):
                if surf.get_at((x, y)).a != 0:
                    draw_surf.set_at((x, y), overlay_color)


        get_window().blit(draw_surf, rect)
        return valid


    def draw_sprites(self) -> None:
        """
        Draw all sprites.

        :param selected_tower: Tower that will be placed.
        :return: Returns nothing.
        """

        self.draw()
        self.draw_enemies()
        self.draw_towers()
        self.draw_projectiles()
    

    def place_tower(self, selected_tower: Tower) -> None:
        """
        Places a tower when in valid location and left mouse up.

        :param selected_tower: Tower to place.
        :return: Returns nothing.
        """

        balance = get_balance()

        # check if valid placement
        if not self.draw_tower_placement(selected_tower):
            return
        # check if left mouse button clicked
        if not get_mouse_up():
            return
        # check if balance is high enough
        if balance < selected_tower.get_cost():
            return
        
        self.add_tower(selected_tower)
        
        balance -= selected_tower.get_cost()


    def update(self) -> None:
        """
        Updates all sprites
        
        :return: Returns nothing.
        """
        
        # win if last wave cleared
        if self.current_wave == len(self.waves) and len(self.track) == 0:
            print("You win!")
            return

        # update projectiles
        for tower in self.towers:
            tower.attack(list(self.track))
            for projectile in tower.projectiles:
                projectile.update()


        # add enemies from wave
        if len(self.waves) > self.current_wave:
            self.waves[self.current_wave].update()


        # update enemies
        self.track.update()

        
    def draw(self) -> None:
        """
        Draws the map sprite.

        :return: Returns nothing.
        """

        get_window().blit(self.image, self.rect)