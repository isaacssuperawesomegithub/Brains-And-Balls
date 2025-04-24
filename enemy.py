"""
Class for the base of enemies. Should be `super()`ed and then have additional modifications.
"""

import pygame
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Stuff to draw the sprite to the screen

        self.surf = pygame.image.load("./art/base zombie.png")
        self.surf.fill((255,23,23))
        self.rect = self.surf.get_rect()

        self.pos = pygame.math.Vector2(0,0)

        self.rect.midbottom = self.pos

        # Enemy Stats

        self.hp = 10
        self.value = 10


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
        return self.pos
    
    def draw(self, window: pygame.surface.Surface) -> None:
        window.blit(self.surf, self.rect)

    def damage(self, amount: int) -> None:
        self.hp -= amount