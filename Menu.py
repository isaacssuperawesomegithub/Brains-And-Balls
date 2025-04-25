import pygame
import sys

pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# Setting the display mode to windowed fullscreen 
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
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

# Load and scale images once
zombie_hand_img = pygame.image.load("art/zombie-hand.png").convert_alpha()
soccer_ball_img = pygame.image.load("art/soccer-ball.png").convert_alpha()
vs_img = pygame.image.load("art/VS.png").convert_alpha()

hand_size = (screen_width // 4, screen_height // 3)
ball_size = (screen_width // 4, screen_height // 3)
vs_size = (screen_width // 8, screen_height // 6)

zombie_hand_img = pygame.transform.scale(zombie_hand_img, hand_size)
soccer_ball_img = pygame.transform.scale(soccer_ball_img, ball_size)
vs_img = pygame.transform.scale(vs_img, vs_size)


def draw_menu():
    screen.fill((0, 0, 0))

    screen.blit(zombie_hand_img, (int(screen_width * 0.65), int(screen_height * 0.55)))
    screen.blit(soccer_ball_img, (int(screen_width * 0.2), int(screen_height * 0.55)))
    screen.blit(vs_img, (screen_width // 2 - vs_size[0] // 2, int(screen_height * 0.6)))

    font_big = pygame.font.Font(None, screen_width // 10)
    font_medium = pygame.font.Font(None, screen_width // 15)
    title = font_big.render("Brains n Balls", True, (255, 255, 255))
    play_button = font_medium.render("START", True, (0, 255, 0))

    title_rect = title.get_rect(center=(screen_width // 2, screen_height // 4))
    button_rect = play_button.get_rect(center=(screen_width // 2, screen_height // 2))

    screen.blit(title, title_rect)
    screen.blit(play_button, button_rect)

    return button_rect


def draw_map():
    screen.fill((30, 30, 30))
    map_title = font.render("Choose a Map", True, (255, 255, 255))
    screen.blit(map_title, (screen_width // 2 - 100, 100))

    map1_button = font.render("Map 1", True, (0, 255, 0))
    map2_button = font.render("Map 2", True, (0, 255, 0))
    map3_button = font.render("Map 3", True, (0, 255, 0))

    rect1 = map1_button.get_rect(center=(screen_width // 4, 250))
    rect2 = map2_button.get_rect(center=(screen_width // 2, 250))
    rect3 = map3_button.get_rect(center=(3 * screen_width // 4, 250))

    screen.blit(map1_button, rect1)
    screen.blit(map2_button, rect2)
    screen.blit(map3_button, rect3)

    return rect1, rect2, rect3


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
        rect1, rect2, rect3 = draw_map()
        if mouse_click:
            if rect1.collidepoint(mouse_pos):
                state = MAP1
            elif rect2.collidepoint(mouse_pos):
                state = MAP2
            elif rect3.collidepoint(mouse_pos):
                state = MAP3

    elif state == MAP1:
        screen.fill((0, 100, 0))
        text = font.render("MAP 1 START", True, (0, 255, 0))
        screen.blit(text, (300, 280))

    elif state == MAP2:
        screen.fill((0, 200, 0))
        text = font.render("MAP 2 START", True, (0, 255, 0))
        screen.blit(text, (300, 280))

    elif state == MAP3:
        screen.fill((0, 255, 0))  # Fixed invalid RGB
        text = font.render("MAP 3 START", True, (0, 255, 0))
        screen.blit(text, (300, 280))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
