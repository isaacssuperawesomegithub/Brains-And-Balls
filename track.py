import pygame
from utils import *

class Track(pygame.sprite.Group):
    def __init__(self, targets: list[pygame.math.Vector2]):
        super().__init__()
        self.targets = targets


    def update(self) -> None:
        """
        Updates the position of all enemies and changes their direction if needed. Draws all enemies.

        :return: Returns nothing.
        """
        
        
        for enemy in self:
            
            if not enemy.target: # set the enemy's target to the first target on the list
                enemy.target = self.targets[0].copy()
            
            if enemy.target == self.targets[-1] or not enemy.target: # stop the enemy from receiving new targets 
                enemy.update(None)

            else: # once the enemy reaches its target, assign it a new one
                enemy.update(self.targets[list(self.targets).index(enemy.target) + 1].copy())
