import pygame
from utils import *
from enemy import Enemy
from projectile import Projectile

class Tower:
    def __init__(self, x: int, y: int, size: int, range: int, damage: int):
        self.x = x
        self.y = y
        self.size = size
        self.range = range
        self.damage = damage


    # returns x, y location
    def get_pos(self) -> tuple[int, int]:
        return self.x, self.y
    
    
    # returns size (radius)
    def get_size(self) -> int:
        return self.size
    

    # returns range
    def get_range(self) -> int:
        return self.range
    

    # returns distance from pos
    def get_distance_from(self, pos):
        x, y = pos
        return ((abs(self.x - x) ** 2) + (abs(self.y - y) ** 2)) ** .5


    # returns whether a point is within the tower's range
    def within_range(self, pos):
        return self.get_distance_from(pos) <= self.range


    # draws a circle at the location
    def draw(self) -> None:
        pygame.draw.circle(get_window(), (10, 200, 80), (self.x, self.y), self.size)

    def get_closest_enemy(self, players: list[Enemy]) -> Enemy:
        closest = None
        for player in players:
            x = self.get_distance_from(player.get_pos())
            if closest == None:
                closest = player
            if closest > x:
                closest = player

    def attack(self, player: list[Enemy] | Enemy) -> None:
        
        if isinstance(player, list):   
            closest = self.get_closest_enemy(player)            
        else:
            closest = player

        if get_distance(player.get_pos(), self.get_pos()) <= self.range:
            self.fire_at(closest)

    def fire_at(self, target: Enemy):
        return Projectile(target, 5)