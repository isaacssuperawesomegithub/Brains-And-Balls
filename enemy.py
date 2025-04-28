"""
Class for the base of enemies. Should be `super()`ed and then have additional modifications.
"""

import pygame
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.math.Vector2, speed: float):
        super().__init__()
        
        # Stuff to draw the sprite to the screen

        self.pos = pos

        self.image = pygame.image.load("./art/base-zombie.png")
        self.rect = self.image.get_rect()

        self.rect.center = self.pos

        # Enemy movement

        self.speed = speed
        self.target = None

        # Enemy Stats

        self.hp = 10
        self.value = 10


    def update(self, new_target: pygame.math.Vector2 | None):
        """
        Updates the enemy sprite to a new position, going the direction of its current target. If the target is reached, the new target will be assigned.

        :param new_target: Target to be set when the sprite reaches its previous target. None if there is no new target.
        :return: Returns nothing.
        """

        if self.target is None and new_target is not None: # sets the enemy's first target
            self.target = new_target

        if self.target is None: return # prevents enemy from moving if it doesn't have a target

        direction = self.target - self.pos # get the direction the enemy needs to travel
        distance = direction.length() # gets the distance between the enemy and its target

        # moves the enemy if it hasn't reached its target
        if distance > 0:
            direction = direction.normalize() # keeps direction length = 1
            self.pos += direction * self.speed

        if distance <= self.speed: # if enemy is close to target
            self.pos = self.target
            if new_target is not None: # sets new target
                self.target = new_target
        
        self.rect.center = self.pos # updates the sprites position


    def die(self, points: int) -> None:
        """
        A function to check if the enemy needs to die or not. If yes, `kill`s the sprite and increases points.

        :param points: The number of points the player has.
        :return: Returns nothing.
        """

        if self.hp <= 0:
            points += self.value
            self.kill()


    def attack(self) -> None:
        """
        A function to register an attack on the total lives remaining.

        :return: Returns Nothing
        """
        pass


    def get_pos(self) -> pygame.math.Vector2:
        """
        Gets the position of the enemy.

        :return: Returns a coordinate reprenting the enemy's position.
        """

        return self.pos
    
    def damage(self, amount: int) -> None:
        """
        Reduces the hp of the enemy.

        :param amount: Amount to reduce enemy hp by.
        :return: Returns nothing.
        """

        self.hp -= amount