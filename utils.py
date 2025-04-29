import pygame
from math import hypot

def get_mouse_pos() -> tuple[int, int]:
    """
    Get the position of the mouse cursor (relative to the display window).

    :return: Returns a tuple coordinate of the cursor position.    
    """

    mouse_x, mouse_y = pygame.mouse.get_pos()

    display_w, display_h = pygame.display.get_surface().get_size()

    window_w, window_h = get_window().get_size()

    return mouse_x * (window_w / display_w), mouse_y * (window_h / display_h)


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
    Gets the unscaled window (to blit onto).

    :return: Returns the surface of the display window.
    """

    from main import window
    return window


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


def get_distance_from_line(line_start: pygame.Vector2, line_end: pygame.Vector2, point: pygame.Vector2) -> float:
    """
    Gets the shortest distance of a point from a line.

    :param line_start: Position of start of line.
    :param line_end: Position of end of line.
    :point: Position of point.
    :return: Returns the distance as a float.
    """
    
    x1, y1 = line_start
    x2, y2 = line_end
    x3, y3 = point

    dx = x2 - x1
    dy = y2 - y1

    if dx == dy == 0: # line is a single point
        return hypot(x3 - x1, y3 - y1)
    
    # how far along the line the point is 
    t = ((x3 - x1) * dx + (y3 - y1) * dy) / (dx ** 2 + dy ** 2)

    # clamp t from 0 to 1
    t = max(0, min(1, t))

    closest_x = x1 + t * dx
    closest_y = y1 + t * dy

    return hypot(x3 - closest_x, y3 - closest_y)