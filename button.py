import pygame
from utils import *

class Button:
    def __init__(self, size, pos, color, img=None):
        self.surf = pygame.surface.Surface(size)
        self.surf.fill(color)
        self.pos = pos
        self.img_surface = img

        self.rect = self.surf.get_rect()
        self.rect.center = self.pos

    def draw_img(self, window):
        window.blit(self.surf, self.rect)
        window.blit(self.img_surface, self.img_surface.get_rect())

    def is_clicked(self):
        if get_mouse_pos() and self.rect.collidepoint(get_mouse_pos()):
            return True
        return False