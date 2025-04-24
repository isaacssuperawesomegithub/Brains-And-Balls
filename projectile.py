import pygame
from math import hypot
from enemy import Enemy
class Projectile(pygame.sprite.Sprite):
    def __init__(self,  target: Enemy, damage: int):
        super().__init__()

        self.surf = pygame.surface.Surface((5,5))
        self.surf.fill((100,100,100))
        self.rect = self.surf.get_rect()
        self.damage = damage

        self.target = target
        self.target_pos = self.target.get_pos()
    def move(self) -> None:
        """
        Moves the projectile towards the target following the hypotenuse of their 2-dimensional distances.

        :return: Returns nothing.
        """

        # Calculates a horizontal line distance between the projectile and the target.
        dx = self.pos.x - self.target_pos.x
        dy = self.pos.y - self.target_pos.y

        # Calculates the hypotenuse of this triangle
        dist = hypot(dx, dy)

        # Avoids divison by zero
        if dist != 0:
            dx /= dist
            dy /= dist

        # Moves along the hypotenuse
        self.pos.x += dx * 5
        self.pos.y += dy * 5

        # If within 5 of the target, dissapears
        if dist <= 5:
            self.kill()
            self.target.damage(self.damage)