import pygame
from utils import *

class Button:
    def __init__(self, size, pos, color, img: pygame.surface.Surface):
        self.surf = pygame.surface.Surface(size)
        self.surf.fill(color)
        self.pos = pos
        self.img_surface = img
        self.img_surface = pygame.transform.scale(self.img_surface, self.surf.get_size())

        self.rect = self.surf.get_rect()
        self.rect.center = self.pos

        self.img_rect = self.img_surface.get_rect()
        self.img_rect.center = self.rect.center

    def draw_img(self, window):
        window.blit(self.surf, self.rect)
        window.blit(self.img_surface, self.img_rect)

    def is_clicked(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(get_mouse_pos()):
            return True
        return False