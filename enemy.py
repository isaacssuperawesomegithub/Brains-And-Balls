"""
Class for the base of enemies. Should be `super()`ed and then have additional modifications.
"""

import pygame
from pygame.locals import *
from utils import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Stuff to draw the sprite to the screen

        self.pos = pygame.Vector2(0, 0)

        self.image = pygame.image.load("./art/base-zombie.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()

        self.rect.center = self.pos

        # Enemy movement

        self.speed = 2
        self.target = None

        # Enemy Stats

        self.hp = 10
        self.value = 10

    
    def set_pos(self, new_pos: pygame.Vector2):
        """
        Sets the position of the enemy.

        :param new_pos: New position.
        :return: Returns nothing.
        """
        self.pos = new_pos
        self.rect.center = self.pos


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


    def at_end(self, final_target: pygame.math.Vector2) -> bool:
        return self.get_pos() == final_target


    def die(self, final_target: pygame.Vector2) -> None:
        """
        A function to check if the enemy needs to die or not. If yes, `kill`s the sprite and increases points or decreases health.

        :param final_target: Final target of the map to determine when the enemy has reached the end.
        :return: Returns nothing.
        """

        if self.hp <= 0:
            balance = get_balance()
            balance += self.value
            self.kill()
            del self
            return
        
        if self.at_end(final_target):
            health = get_health()
            health -= 1
            self.kill()
            del self


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

class Enemy1(Enemy):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("./art/white-soccer.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()

        self.speed = 2

        self.hp = 10
        self.value = 15

class Enemy2(Enemy):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("./art/red-soccer.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()

        self.speed = 4

        self.hp = 5
        self.value = 10

class Enemy3(Enemy):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("./art/#10-soccer-player.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()

        self.speed = .5

        self.hp = 50
        self.value = 25