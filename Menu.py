import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 40)
just_entered_map = False
previous_state = None  # Add previous_state definition here

# Game states
MENU = "MENU"
MAPS = "MAP"
MAP1 = "MAP1"
MAP2 = "MAP2"
MAP3 = "MAP3"
PAUSE = "PAUSE"
state = MENU


def draw_menu():
    screen.fill((30, 30, 30))
    title = font.render("Brains n Balls", True, (255, 255, 255))
    play_button = font.render("START", True, (0, 255, 0))
    screen.blit(title, (290, 100))
    screen.blit(play_button, (350, 250))
    return pygame.Rect(350, 250, play_button.get_width(), play_button.get_height())


def draw_mapscreen():
    screen.fill((30, 30, 30))
    map_title = font.render("Choose a Map", True, (255, 255, 255))
    screen.blit(map_title, (270, 100))
    
    map_button = font.render("Map 1", True, (0, 255, 0))
    map_button2 = font.render("Map 2", True, (0, 255, 0))
    map_button3 = font.render("Map 3", True, (0, 255, 0))
    
    screen.blit(map_button, (100, 250))
    screen.blit(map_button2, (350, 250))
    screen.blit(map_button3, (600, 250))

    rect1 = pygame.Rect(100, 250, map_button.get_width(), map_button.get_height())
    rect2 = pygame.Rect(350, 250, map_button2.get_width(), map_button2.get_height())
    rect3 = pygame.Rect(600, 250, map_button3.get_width(), map_button3.get_height())
    
    return rect1, rect2, rect3


def draw_pause_button():
    pause_button = font.render("Pause", True, (255, 255, 255))
    screen.blit(pause_button, (700, 10))
    return pygame.Rect(700, 10, pause_button.get_width(), pause_button.get_height())


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

    # Menu state (main menu)
    if state == MENU:
        button_rect = draw_menu()
        if mouse_click and button_rect.collidepoint(mouse_pos):
            state = MAPS

    # Map selection screen
    elif state == MAPS:
        rect1, rect2, rect3 = draw_mapscreen()
        if mouse_click:
            if rect1.collidepoint(mouse_pos):
                state = MAP1
                just_entered_map = True
            elif rect2.collidepoint(mouse_pos):
                state = MAP2
                just_entered_map = True
            elif rect3.collidepoint(mouse_pos):
                state = MAP3
                just_entered_map = True

    # Map 1
    elif state == MAP1:
        screen.fill((0, 0, 200))
        text = font.render("MAP 1 START", True, (0, 255, 0))
        screen.blit(text, (300, 280))

        # Draw the pause button
        pause_rect = draw_pause_button()

        # Handle pause click (only if it's not the first frame of entering the map)
        if mouse_click and not just_entered_map and pause_rect.collidepoint(mouse_pos):
            previous_state = state  # Save the current state before pausing
            state = PAUSE

        # Reset the flag after first frame
        just_entered_map = False

    # Map 2
    elif state == MAP2:
        screen.fill((0, 100, 0))
        text = font.render("MAP 2 START", True, (0, 255, 0))
        screen.blit(text, (300, 280))

        # Draw the pause button
        pause_rect = draw_pause_button()

        # Handle pause click (only if it's not the first frame of entering the map)
        if mouse_click and not just_entered_map and pause_rect.collidepoint(mouse_pos):
            previous_state = state  # Save the current state before pausing
            state = PAUSE

        # Reset the flag after first frame
        just_entered_map = False

    # Map 3
    elif state == MAP3:
        screen.fill((0, 250, 0))
        text = font.render("MAP 3 START", True, (0, 0, 0))
        screen.blit(text, (300, 280))

        # Draw the pause button
        pause_rect = draw_pause_button()

        # Handle pause click (only if it's not the first frame of entering the map)
        if mouse_click and not just_entered_map and pause_rect.collidepoint(mouse_pos):
            previous_state = state  # Save the current state before pausing
            state = PAUSE

        # Reset the flag after first frame
        just_entered_map = False

    # Pause screen
    elif state == PAUSE:
        screen.fill((20, 20, 20))
        text = font.render("PAUSED", True, (0, 250, 0))
        screen.blit(text, (300, 100))
        
        # Draw resume button
        resume_button = font.render("Resume", True, (0, 255, 0))
        screen.blit(resume_button, (350, 300))
        resume_rect = pygame.Rect(350, 300, resume_button.get_width(), resume_button.get_height())

        # Draw Menu button
        menu_button = font.render("Menu", True, (0, 255, 0))
        screen.blit(resume_button, (350, 200))
        menu_rect = pygame.Rect(350, 200, menu_button.get_width(), menu_button.get_height())

        if mouse_click and menu_rect.collidepoint(mouse_pos):
            state = previous_state  # Return to the previous state when "Resume" is clicked

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
