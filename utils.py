import pygame
from balance import Balance
from health import Health
from math import hypot

def get_mouse_pos() -> pygame.Vector2:
    """
    Get the position of the mouse cursor (relative to the display window).

    :return: Returns a tuple coordinate of the cursor position.    
    """

    mouse_x, mouse_y = pygame.mouse.get_pos()

    display_w, display_h = pygame.display.get_surface().get_size()

    window_w, window_h = get_window().get_size()

    return pygame.Vector2(mouse_x * (window_w / display_w), mouse_y * (window_h / display_h))


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

    :return: Returns the surface of the usncaled window.
    """

    from main import window
    return window


def get_fullscreen() -> pygame.Surface:
    """
    Gets the scaled window. Useful for maintaining quality of things like text.

    :return: Returns the surface of the scaled window.
    """

    return pygame.display.get_surface()


def get_scale() -> tuple[int, int]:
    """
    Gets the scale of the unscaled window to the scaled window.

    :return: Returns a tuple of the scale for the width and height.
    """

    return get_fullscreen().width / get_window().width, get_fullscreen().height / get_window().height


def scale_pos(to_scale: pygame.Vector2 | tuple | pygame.Rect) -> pygame.Vector2 | tuple | pygame.Rect:
    """
    Gets the scaled position or Rect from a unscaled position or Rect.

    :param to_scale: Coordinate or Rect to scale.
    :return: Returns a vector, tuple, or Rect depending on type of argument.
    """
    
    x_scale, y_scale = get_scale()
    
    if type(to_scale) == pygame.Rect:
        rect = pygame.Rect(to_scale.x * x_scale, to_scale.y * y_scale, to_scale.width, to_scale.height)
        x, y = to_scale.center
        rect.center = x * x_scale, y * y_scale
        return rect
    
    return type(to_scale)((to_scale[0] * x_scale, to_scale[1] * y_scale))


def draw_text(text: str, pos: tuple[int, int], font: str=None, size:int =20, color: tuple[int, int, int]=(255, 255, 255), alignment: str="center") -> None:
    """
    Draws text on display screen, scales with screen size.

    :param text: Text to draw.
    :param pos: Position of text.
    :param font: Font to use.
    :param size: Size of text.
    :param color: Color of text.
    :param: alignment: Alignment of text.

    :return: Returns nothing.
    """

    font = pygame.Font(font, round(size * (get_fullscreen().get_height() / 1000)))

    text = font.render(text, True, color)
    text_rect = text.get_rect()
    match alignment:
        case "center":
            text_rect.center = scale_pos(pos)
        case "midleft":
            text_rect.midleft = scale_pos(pos)
        case "midright":
            text_rect.midright = scale_pos(pos)
        case "topleft":
            text_rect.topleft = scale_pos(pos)
        case "topright":
            text_rect.topright = scale_pos(pos)

        case _:
            raise(TypeError("Not a valid alignment."))

    get_fullscreen().blit(text, text_rect)


def get_balance() -> Balance:
    """
    Gets most recently defined instance of balance.

    :return: Returns balance.
    """

    try:
        return Balance.instance
    except AttributeError:
        raise TypeError("No balance object initialized.")

def get_health() -> Health:
    """
    Gets most recently defined instance of health.

    :return Returns health.
    """

    try:
        return Health.instance
    except AttributeError:
        raise TypeError("No health object initialized.")


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