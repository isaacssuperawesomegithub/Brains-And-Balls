import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen Setup
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()

# Fonts
menu_font = pygame.font.SysFont("Times New Roman", 40)
map_font = pygame.font.SysFont("Arial", 36)

# Game States
MENU = "MENU"
MAPS = "MAPS"
MAP1 = "MAP1"
MAP2 = "MAP2"
MAP3 = "MAP3"
PAUSE = "PAUSE"
state = MENU
previous_state = None
just_entered_map = True

# Currency
currency = 100  # Starting money

# Load Images
zombie_hand_img = pygame.image.load("art/zombie-hand.png").convert_alpha()
soccer_ball_img = pygame.image.load("art/soccer-ball.png").convert_alpha()
vs_img = pygame.image.load("art/VS.png").convert_alpha()
background_map1 = pygame.image.load("art/map1.png").convert_alpha()

# Scale Images
zombie_hand_img = pygame.transform.scale(zombie_hand_img, (screen_width // 4, screen_height // 3))
soccer_ball_img = pygame.transform.scale(soccer_ball_img, (screen_width // 4, screen_height // 3))
vs_img = pygame.transform.scale(vs_img, (screen_width // 8, screen_height // 6))
background_map1 = pygame.transform.scale(background_map1, (screen_width, screen_height))

# Tower Icons (now with cost!)
tower_icons = [
    {"color": (255, 0, 0), "rect": pygame.Rect(100, screen_height - 100, 60, 60), "cost": 20},  # Base Zombie Tower
    {"color": (0, 255, 0), "rect": pygame.Rect(200, screen_height - 100, 60, 60), "cost": 30},  # Zombie2 Tower
]

# Dragging variables
dragging_tower = False
dragged_tower_color = None
dragged_tower_pos = (0, 0)
dragged_tower_cost = 0  # NEW

# List of placed towers
placed_towers = []

# Functions
def draw_menu():
    screen.fill((0, 0, 0))
    screen.blit(zombie_hand_img, (screen_width // 4 - zombie_hand_img.get_width() // 2, screen_height // 2 - zombie_hand_img.get_height() // 2))
    screen.blit(soccer_ball_img, (3 * screen_width // 4 - soccer_ball_img.get_width() // 2, screen_height // 2 - soccer_ball_img.get_height() // 2))
    screen.blit(vs_img, (screen_width // 2 - vs_img.get_width() // 2, screen_height // 2 - vs_img.get_height() // 2))

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

def draw_bottom_menu():
    menu_height = 100
    pygame.draw.rect(screen, (50, 50, 50), (0, screen_height - menu_height, screen_width, menu_height))
    for tower in tower_icons:
        pygame.draw.rect(screen, tower["color"], tower["rect"])
        # Draw cost above each tower
        cost_text = map_font.render(f"${tower['cost']}", True, (255, 255, 255))
        cost_rect = cost_text.get_rect(center=(tower["rect"].centerx, tower["rect"].top - 20))
        screen.blit(cost_text, cost_rect)

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

        # Draw Currency
        currency_text = map_font.render(f"Money: ${currency}", True, (255, 255, 0))
        screen.blit(currency_text, (30, 30))

        for tower in placed_towers:
            pygame.draw.circle(screen, tower["color"], tower["pos"], 20)

        # Draw dragged tower
        if dragging_tower and dragged_tower_color:
            pygame.draw.circle(screen, dragged_tower_color, mouse_pos, 20)

        map1_label = map_font.render("MAP 1 START", True, (255, 255, 255))
        screen.blit(map1_label, (screen_width // 2 - map1_label.get_width() // 2, 80))

        pause_rect = draw_pause_button()

        draw_bottom_menu()

        if mouse_click and not just_entered_map:
            for tower in tower_icons:
                if tower["rect"].collidepoint(mouse_pos):
                    if currency >= tower["cost"]:  # Check specific tower cost
                        dragging_tower = True
                        dragged_tower_color = tower["color"]
                        dragged_tower_cost = tower["cost"]

            if pause_rect.collidepoint(mouse_pos):
                previous_state = state
                state = PAUSE

        just_entered_map = False

        # If releasing mouse button (drop the tower)
        if dragging_tower and not pygame.mouse.get_pressed()[0]:  # Left mouse button released
            if mouse_pos[1] < screen_height - 100:  # Not inside menu area
                placed_towers.append({"color": dragged_tower_color, "pos": mouse_pos})
                currency -= dragged_tower_cost  # Deduct the specific cost
            dragging_tower = False
            dragged_tower_color = None
            dragged_tower_cost = 0

    elif state == MAP2:
        screen.fill((100, 0, 0))
        map2_label = map_font.render("MAP 2 START", True, (255, 255, 255))
        screen.blit(map2_label, (screen_width // 2 - map2_label.get_width() // 2, screen_height // 2))

        pause_rect = draw_pause_button()
        if mouse_click and not just_entered_map and pause_rect.collidepoint(mouse_pos):
            previous_state = state
            state = PAUSE

        just_entered_map = False

    elif state == MAP3:
        screen.fill((0, 100, 0))
        map3_label = map_font.render("MAP 3 START", True, (255, 255, 255))
        screen.blit(map3_label, (screen_width // 2 - map3_label.get_width() // 2, screen_height // 2))

        pause_rect = draw_pause_button()
        if mouse_click and not just_entered_map and pause_rect.collidepoint(mouse_pos):
            previous_state = state
            state = PAUSE

        just_entered_map = False

    elif state == PAUSE:
        screen.fill((20, 20, 20))
        paused_label = menu_font.render("PAUSED", True, (0, 255, 0))
        screen.blit(paused_label, (screen_width // 2 - paused_label.get_width() // 2, 100))

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
                state = MENU

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
