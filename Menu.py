import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((2560, 1920))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 40)

# Game states
MENU = "MENU"
MAPS = "MAP"
MAP1 = "MAP1"
MAP2 = "MAP2"
MAP3 = "MAP3"
state = MENU

import pygame

def draw_menu():
    screen.fill((0, 0, 0))

    # background images
    zombie_hand = pygame.image.load(r"C:\Users\gci.232222\OneDrive - geneseeisd.org\pygame\Brains and Balls\Brains-And-Balls\art\zombie-hand.png").convert_alpha()
    soccer_ball = pygame.image.load(r"C:\Users\gci.232222\OneDrive - geneseeisd.org\pygame\Brains and Balls\Brains-And-Balls\art\soccer-ball.png").convert_alpha()
    vs = pygame.image.load(r"C:\Users\gci.232222\OneDrive - geneseeisd.org\pygame\Brains and Balls\Brains-And-Balls\art\VS.png").convert_alpha()

    # size
    zombie_hand = pygame.transform.scale(zombie_hand, (700, 700))
    soccer_ball = pygame.transform.scale(soccer_ball, (700, 700))
    vs = pygame.transform.scale(vs, (300, 300))

    # Draw both images
    screen.blit(zombie_hand, (1500, 800))   
    screen.blit(soccer_ball, (500, 750))
    screen.blit(vs, (1100, 870)) 

    # Draw title and play button
    font = pygame.font.Font(None, 250)  #font size
    title = font.render("Brains n Balls", True, (255, 255, 255))
    play_button = font.render("START", True, (0, 255, 0))
    screen.blit(title, (585, 300))
    screen.blit(play_button, (980, 600))




    return pygame.Rect(350, 250, play_button.get_width(), play_button.get_height())



def draw_map():
    screen.fill((30, 30, 30))
    map_title = font.render("Choose a Map", True, (255, 255, 255))
    screen.blit(map_title, (270, 100))
    map_button = font.render("Map 1", True, (0, 255, 0))
    map_button2 = font.render("Map 2", True, (0, 255, 0))
    map_button3 = font.render("Map 3", True, (0, 255, 0))
    screen.blit(map_button, (100, 250))
    screen.blit(map_button2, (350, 250))
    screen.blit(map_button3, (600, 250))
    return pygame.Rect(350, 250, map_button.get_width(), map_button.get_height())
    return pygame.Rect(350, 250, map_button2.get_width(), map_button2.get_height())

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True

    if state == MENU:
        button_rect = draw_menu()
        if mouse_click and button_rect.collidepoint(mouse_pos):
            state = MAPS

    elif state == MAPS:
        map_rect = draw_map()
        if mouse_click and map_rect.collidepoint(mouse_pos):
            state = MAP1 

    elif state == MAP1:
        screen.fill((0, 100, 0))
        text = font.render("MAP 2 START", True, (0, 255, 0))
        screen.blit(text, (300, 280))
    
    elif state == MAP2:
        screen.fill((0, 200, 0))
        text = font.render("MAP 2 START", True, (0, 255, 0))
        screen.blit(text, (300, 280))
    
    elif state == MAP3:
        screen.fill((0, 300, 0))
        text = font.render("MAP 3 START", True, (0, 255, 0))
        screen.blit(text, (300, 280))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
