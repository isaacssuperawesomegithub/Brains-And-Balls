import pygame
from utils import *
from typing import Callable

class Button:
    def __init__(self, size, pos, color, img: pygame.surface.Surface, function: Callable=None):
        self.surf = pygame.surface.Surface(size)
        self.surf.fill(color)
        self.pos = pos
        self.img_surface = img
        self.img_surface = pygame.transform.scale(self.img_surface, self.surf.get_size())

        self.rect = self.surf.get_rect()
        self.rect.center = self.pos

        self.img_rect = self.img_surface.get_rect()
        self.img_rect.center = self.rect.center

        self.function = function


    def draw_img(self, window: pygame.Surface) -> None:
        """
        Draws the button and its image to a surface.

        :param window: Surface to blit to.
        :return: Returns nothing.
        """

        window.blit(self.surf, self.rect)
        window.blit(self.img_surface, self.img_rect)


    def update(self, *kwargs) -> bool:
        """
        Calls the function assigned to the button with specified arguments.

        :param kwargs: Arguments to pass through function.
        :return: Returns a boolean, true when the button is pressed.        
        """

        if get_mouse_up() and self.rect.collidepoint(get_mouse_pos()):
            if self.function is not None:
                self.function(*kwargs)
            
            return True
        
        return False