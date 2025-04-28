import pygame
from utils import *
from enemy import Enemy

class Track:
    def __init__(self, targets: list[pygame.math.Vector2]):
        self.targets = targets
        self.enemies = pygame.sprite.Group()


    def add_enemy(self, enemy: Enemy) -> None:
        """
        Add an enemy to the enemies list.
        
        :param enemy: Enemy to be added.
        :return: Returns nothing.
        """

        self.enemies.add(enemy)


    def update_enemies(self) -> None:
        """
        Updates the position of all enemies and changes their direction if needed. Draws all enemies.

        :return: Returns nothing.
        """
        
        for enemy in self.enemies:
            
            if not enemy.target: # set the enemy's target to the first target on the list
                enemy.target = self.targets[0]

            if enemy.target == self.targets[-1] or not enemy.target: # stop the enemy from receiving new targets 
                enemy.update(None)

            else: # once the enemy reaches its target, assign it a new one
                enemy.update(self.targets[self.targets.index(enemy.target) + 1])
                    

    def draw_enemies(self) -> None:
        """
        Draws all enemies on the screen.
        
        :return: Returns nothing.
        """

        self.enemies.draw(get_window())