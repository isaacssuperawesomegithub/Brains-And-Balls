import pygame
from math import hypot

def get_mouse_pos() -> tuple[int, int]:
    """
    Get the position of the mouse cursor.

    :return: Returns a tuple coordinate of the cursor position.    
    """

    return pygame.mouse.get_pos()


def get_mouse_up() -> bool:
    """
    Checks for when the left mouse button is released.

    :return: Returns a boolean that is true when the left mouse button is released.
    """

    from main import events
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
            return True
        
    return False


def get_window() -> pygame.Surface:
    """
    Gets the current display window.

    :return: Returns the surface of the display window.
    """

    return pygame.display.get_surface()


def get_distance(first_pos: pygame.math.Vector2 | list[float, float], second_pos: pygame.math.Vector2| list[float, float]) -> float:
    """
    Finds the distance between two given points.

    :param first_pos: The first point.
    :param second_pos: The second point.
    :return: Returns the hypotenuse distance between the two points.
    """

    # Calculates a horizontal line distance between the projectile and the target.
    dx = first_pos[0] - second_pos[0]
    dy = first_pos[1] - second_pos[1]

    # Calculates the hypotenuse of this triangle
    dist = hypot(dx, dy)
    return dist