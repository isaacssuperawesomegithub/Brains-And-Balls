import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen Setup
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()

# Fonts
menu_font = pygame.font.SysFont("Comic Sans MS", 100)
map_font = pygame.font.SysFont("Comic Sans MS", 36)

# Game States
MENU = "MENU"
MAPS = "MAPS"
MAP1 = "MAP1"
MAP2 = "MAP2"
MAP3 = "MAP3"
PAUSE = "PAUSE"
COUNTDOWN = "COUNTDOWN"  # New state for countdown
WAVE = "WAVE"  # New state for wave
state = MENU
previous_state = None
just_entered_map = True
start_clicked = False

# Load Images
zombie_hand_img = pygame.image.load("art/zombie-hand.png").convert_alpha()
soccer_ball_img = pygame.image.load("art/soccer-ball.png").convert_alpha()
vs_img = pygame.image.load("art/VS.png").convert_alpha()
background_map1 = pygame.image.load("art/map1.png").convert_alpha()

# Scale Images
zombie_hand_img = pygame.transform.scale(zombie_hand_img, (screen_width // 4, screen_height // 3))
soccer_ball_img = pygame.transform.scale(soccer_ball_img, (screen_width // 4, screen_height // 3))
vs_img = pygame.transform.scale(vs_img, (screen_width // 8, screen_height // 6))
background_map1 = pygame.transform.scale(background_map1, (screen_width, screen_height))  # Important!

# Functions
def draw_menu():
    screen.fill((0, 0, 0))

    # Draw "Brains and Balls" at the top
    title_text = menu_font.render("Brains and Balls", True, (255, 255, 255))
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 30))

    # Draw hand, ball, vs
    screen.blit(zombie_hand_img, (screen_width // 4 - zombie_hand_img.get_width() // 2, screen_height // 2 - zombie_hand_img.get_height() // 2))
    screen.blit(soccer_ball_img, (3 * screen_width // 4 - soccer_ball_img.get_width() // 2, screen_height // 2 - soccer_ball_img.get_height() // 2))
    screen.blit(vs_img, (screen_width // 2 - vs_img.get_width() // 2, screen_height // 2 - vs_img.get_height() // 2))

    # Draw Play button
    play_text = menu_font.render("Play", True, (0, 255, 0))
    play_rect = play_text.get_rect(center=(screen_width // 2, screen_height // 2 + 200))
    screen.blit(play_text, play_rect)

    return play_rect

def draw_map_select():
    screen.fill((30, 30, 30))
    title = map_font.render("Choose a Map", True, (255, 255, 255))
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, 100))

    map1_text = map_font.render("Map 1", True, (0, 255, 0))
    map2_text = map_font.render("Map 2", True, (0, 255, 0))
    map3_text = map_font.render("Map 3", True, (0, 255, 0))

    rect1 = map1_text.get_rect(center=(screen_width // 4, 300))
    rect2 = map2_text.get_rect(center=(screen_width // 2, 300))
    rect3 = map3_text.get_rect(center=(3 * screen_width // 4, 300))

    screen.blit(map1_text, rect1)
    screen.blit(map2_text, rect2)
    screen.blit(map3_text, rect3)

    return rect1, rect2, rect3

def draw_pause_button():
    pause_text = map_font.render("Pause", True, (255, 255, 255))
    pause_rect = pause_text.get_rect(topleft=(screen_width - 150, 10))
    screen.blit(pause_text, pause_rect)
    return pause_rect

def draw_wave(wave_number):
    wave_text = map_font.render(f"Wave {wave_number}", True, (255, 255, 255))
    screen.blit(wave_text, (screen_width // 2 - wave_text.get_width() // 2, 30))  # Display wave at top

# Main Loop
running = True

while running:
    mouse_click = False
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True

    if state == MENU:
        play_rect = draw_menu()
        if mouse_click and play_rect.collidepoint(mouse_pos):
            state = MAPS

    elif state == MAPS:
        rect1, rect2, rect3 = draw_map_select()
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

    elif state == MAP1:
        screen.blit(background_map1, (0, 0))
        map1_label = map_font.render("START 0/1", True, (255, 255, 255))
        
        # Update label text based on click
        if start_clicked:
            map1_label = map_font.render("START 1/1", True, (255, 255, 255))

        screen.blit(map1_label, (screen_width // 2 - map1_label.get_width() // 2, 30))

        pause_rect = draw_pause_button()

        if mouse_click and not just_entered_map and pause_rect.collidepoint(mouse_pos):
            previous_state = state
            state = PAUSE

        # Detect click on START label
        if mouse_click and not start_clicked:
            if (screen_width // 2 - map1_label.get_width() // 2 <= mouse_pos[0] <= screen_width // 2 + map1_label.get_width() // 2) and (30 <= mouse_pos[1] <= 30 + map1_label.get_height()):
                start_clicked = True
                state = COUNTDOWN  # Start countdown when "START 1/1" is clicked

        just_entered_map = False

    elif state == COUNTDOWN:
        # Display the map background
        screen.blit(background_map1, (0, 0))

        # Countdown from 3
        countdown_text_3 = menu_font.render("3", True, (255, 255, 255))
        countdown_rect_3 = countdown_text_3.get_rect(center=(screen_width // 2, 50))  # Position at top center
        screen.blit(countdown_text_3, countdown_rect_3)
        pygame.display.flip()
        pygame.time.wait(1000)  # Wait for 1 second

        # Display number 2
        countdown_text_2 = menu_font.render("2", True, (255, 255, 255))
        countdown_rect_2 = countdown_text_2.get_rect(center=(screen_width // 2, 50))  # Position at top center
        screen.blit(countdown_text_2, countdown_rect_2)
        pygame.display.flip()
        pygame.time.wait(1000)  # Wait for 1 second

        # Display number 1
        countdown_text_1 = menu_font.render("1", True, (255, 255, 255))
        countdown_rect_1 = countdown_text_1.get_rect(center=(screen_width // 2, 50))  # Position at top center
        screen.blit(countdown_text_1, countdown_rect_1)
        pygame.display.flip()
        pygame.time.wait(1000)  # Wait for 1 second

        # After countdown finishes, show Wave 1
        draw_wave(1)
        pygame.display.flip()
        pygame.time.wait(1000)  # Wait for a second before transitioning to wave

        state = WAVE  # Once countdown is finished, move to wave display

    elif state == WAVE:
        # Keep the background visible
        screen.blit(background_map1, (0, 0))

        # Draw Wave 1 text
        draw_wave(1)
    
    elif state == PAUSE:
        screen.fill((20, 20, 20))
        paused_label = menu_font.render("PAUSED", True, (0, 255, 0))
        screen.blit(paused_label, (screen_width // 2 - paused_label.get_width() // 2, 100))

        # Resume and Quit buttons
        resume_text = map_font.render("Resume", True, (0, 255, 0))
        resume_rect = resume_text.get_rect(center=(screen_width // 2, 300))
        screen.blit(resume_text, resume_rect)

        quit_text = map_font.render("Quit", True, (255, 0, 0))
        quit_rect = quit_text.get_rect(center=(screen_width // 2, 400))
        screen.blit(quit_text, quit_rect)

        if mouse_click:
            if resume_rect.collidepoint(mouse_pos):
                state = previous_state
            elif quit_rect.collidepoint(mouse_pos):
                # Reset start to "START 0/1" when quitting
                start_clicked = False
                state = MENU  # Go back to the main menu

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
