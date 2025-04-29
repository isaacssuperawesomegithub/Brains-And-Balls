import pygame
from math import hypot
from enemy import Enemy
class Projectile(pygame.sprite.Sprite):
    def __init__(self,  target: Enemy, damage: int, pos: pygame.Vector2):
        super().__init__()

        self.pos = pos

        self.image = pygame.surface.Surface((5, 5))
        self.image.fill((255,100,100))
        self.rect = self.image.get_rect()

        self.rect.center = self.pos

        self.damage = damage

        self.target = target
        self.target_pos = pygame.Vector2(self.target.get_pos())


    def update(self) -> None:
        """
        Moves the projectile towards the target following the hypotenuse of their 2-dimensional distances.

        :return: Returns nothing.
        """

        self.target_pos = pygame.Vector2(self.target.pos)

        # Calculates a horizontal line distance between the projectile and the target.
        dx = self.target_pos.x - self.pos.x
        dy = self.target_pos.y - self.pos.y 

        # Calculates the hypotenuse of this triangle
        dist = hypot(dx, dy)

        # Avoids divison by zero
        if dist != 0:
            dx /= dist
            dy /= dist

        # Moves along the hypotenuse
        self.pos.x += dx * 7
        self.pos.y += dy * 7

        self.rect.center = self.pos

        # If within 5 of the target, dissapears
        if dist <= 5:
            self.kill()
            self.target.damage(self.damage)