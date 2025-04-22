import pygame
from utils import *

class Tower:
    def __init__(self, x: int, y: int, size: int, range: int):
        self.x = x
        self.y = y
        self.size = size
        self.range = range


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
