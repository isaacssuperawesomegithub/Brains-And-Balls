import pygame
import sys

# Initialize pygame
pygame.init()


w = pygame.display.set_mode((400, 400))

# Define Zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((40, 40))
        self.rect = self.surf.get_rect(topleft=(50, 50))
        self.surf.fill((255, 182, 193))  # Light pink

# Define Soccer Player class
class SPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((40, 40))
        self.rect = self.surf.get_rect(topleft=(150, 150))
        self.surf.fill((100, 200, 255))  # Light blue

# Create instances
z = Zombie()
s = SPlayer()

#Game loop (for now)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    w.fill((0, 0, 0))  # Black background

    # Draw sprites
    w.blit(z.surf, z.rect)
    w.blit(s.surf, s.rect)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()