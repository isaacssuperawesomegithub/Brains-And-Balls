import pygame
from math import hypot
from enemy import Enemy
# get mouse position
def get_mouse_pos() -> tuple[int, int]:
    return pygame.mouse.get_pos()

# check for left mouse click
def get_mouse_up() -> bool:
    from main import events
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
            return True
        
    return False

# returns screen to draw on
def get_window():
    return pygame.display.get_surface()

def get_distance(first_pos: pygame.math.Vector2, second_pos: pygame.math.Vector2) -> float:
    """
    Finds the distance between two given sprites.

    :param sprite1: The first sprite.
    :param sprite2: The second sprite.
    :return: Returns the hypotenuse distance between the two sprites.
    """
    # Calculates a horizontal line distance between the projectile and the target.
    dx = first_pos.pos.x - second_pos.get_pos().x
    dy = first_pos.pos.y - second_pos.get_pos().y

    # Calculates the hypotenuse of this triangle
    dist = hypot(dx, dy)
    return dist