import pygame
from utils import *
from enemy import Enemy
from projectile import Projectile

class Tower(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2, size: int, range: int, damage: int):
        super().__init__()
        
        self.pos = pos
        
        self.image = pygame.image.load("./art/icecream-zombie.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()

        self.rect.center = self.pos

        self.size = size
        self.range = range
        self.damage = damage


    def get_pos(self) -> pygame.Vector2:
        """
        Gets the position of the tower.

        :return: Returns a coordinate of the tower's position.
        """

        return self.pos
    
    
    def get_size(self) -> int:
        """
        Gets the size (radius) of the tower.

        :return: Returns an int representing the radius of the tower's size.
        """

        return self.size
    

    def get_range(self) -> int:
        """
        Gets the range (radius) of the tower.

        :return: Returns an int representing the radius of the tower's range.
        """

        return self.range
    

    def get_distance_from(self, pos: pygame.Vector2) -> float:
        """
        Gets the distance from a specified point.

        :param pos: Coordinate to get distance from.
        :return: Returns a float representing the distance from the tower to the point.
        """

        return get_distance(pos, self.get_pos())


    def within_range(self, pos: pygame.Vector2) -> bool:
        """
        Checks if a point is within the tower's range.

        :param pos: Position to check if within range.
        :return: Returns a boolean, True if point is within range.
        """

        return self.get_distance_from(pos) <= self.range


    def get_closest_enemy(self, players: list[Enemy]) -> Enemy:
        """
        Gets the enemy closest to the tower.

        :param players: List of enemies to get closest from.
        :return: Returns the closest enemy.
        """

        closest = None
        for player in players:
            x = self.get_distance_from(player.get_pos())
            if closest == None or closest > x:
                closest = player


    def attack(self, player: list[Enemy] | Enemy) -> None:
        """
        Calls `Fire_at` on the specified enemy or closest enemy within a list.

        :param player: Enemy of list of enemys to fire at.
        :return: Returns nothing.
        """

        if isinstance(player, list):   
            player = self.get_closest_enemy(player)            

        if self.get_distance_from(player.get_pos()) <= self.range:
            self.fire_at(player)


    def fire_at(self, target: Enemy):
        return Projectile(target, 5)