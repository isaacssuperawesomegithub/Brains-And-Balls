import pygame

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