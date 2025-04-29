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
menu_font = pygame.font.SysFont("Comic Sans MS", 100)
map_font = pygame.font.SysFont("Comic Sans MS", 36)

# Game States
MENU = "MENU"
MAPS = "MAPS"
MAP1 = "MAP1"
MAP2 = "MAP2"
MAP3 = "MAP3"
PAUSE = "PAUSE"
COUNTDOWN = "COUNTDOWN"
WAVE = "WAVE"
state = MENU
previous_state = None
just_entered_map = True
start_clicked = False

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

# Tower Icons
tower_icons = [
    {"color": (255, 0, 0), "rect": pygame.Rect(100, screen_height - 100, 60, 60), "cost": 20},
    {"color": (0, 255, 0), "rect": pygame.Rect(200, screen_height - 100, 60, 60), "cost": 30},
]

# Dragging
dragging_tower = False
dragged_tower_color = None
dragged_tower_pos = (0, 0)
dragged_tower_cost = 0

# Placed towers
placed_towers = []

# Enemies
class Enemy:
    def __init__(self, path):
        self.path = path
        self.current_point = 0
        self.pos = list(path[0])
        self.speed = 2
        self.hp = 100

    def move(self):
        if self.current_point < len(self.path) - 1:
            target = self.path[self.current_point + 1]
            dx, dy = target[0] - self.pos[0], target[1] - self.pos[1]
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist != 0:
                dx /= dist
                dy /= dist
                self.pos[0] += dx * self.speed
                self.pos[1] += dy * self.speed
            if dist < self.speed:
                self.current_point += 1

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 255), (int(self.pos[0]), int(self.pos[1])), 15)

enemy_path = [(0, 300), (300, 300), (600, 300), (900, 500), (1200, 300)]
enemies = []

# === UI Functions ===
def draw_menu():
    screen.fill((0, 0, 0))
    title_text = menu_font.render("Brains and Balls", True, (255, 255, 255))
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 30))

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

    map_texts = ["Map 1", "Map 2", "Map 3"]
    positions = [screen_width // 4, screen_width // 2, 3 * screen_width // 4]
    rects = []

    for i, text in enumerate(map_texts):
        rendered = map_font.render(text, True, (0, 255, 0))
        rect = rendered.get_rect(center=(positions[i], 300))
        screen.blit(rendered, rect)
        rects.append(rect)

    return rects

def draw_pause_button():
    pause_text = map_font.render("Pause", True, (255, 255, 255))
    pause_rect = pause_text.get_rect(topleft=(screen_width - 150, 10))
    screen.blit(pause_text, pause_rect)
    return pause_rect

def draw_bottom_menu():
    pygame.draw.rect(screen, (50, 50, 50), (0, screen_height - 100, screen_width, 100))
    for tower in tower_icons:
        pygame.draw.rect(screen, tower["color"], tower["rect"])
        cost_text = map_font.render(f"${tower['cost']}", True, (255, 255, 255))
        cost_rect = cost_text.get_rect(center=(tower["rect"].centerx, tower["rect"].top - 20))
        screen.blit(cost_text, cost_rect)

def draw_wave(wave_number):
    wave_text = map_font.render(f"Wave {wave_number}", True, (255, 255, 255))
    screen.blit(wave_text, (screen_width // 2 - wave_text.get_width() // 2, 30))

# === Main Game Loop ===
running = True
wave_number = 1
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

    if state in [MAP1, COUNTDOWN, WAVE]:
        screen.blit(background_map1, (0, 0))
        currency_text = map_font.render(f"Money: ${currency}", True, (255, 255, 0))
        screen.blit(currency_text, (30, 30))
        pause_rect = draw_pause_button()
        draw_bottom_menu()

        # START button
        if state == MAP1:
            label_text = "START 1/1" if start_clicked else "START 0/1"
            map1_label = map_font.render(label_text, True, (255, 255, 255))
            map1_rect = map1_label.get_rect(center=(screen_width // 2, 30))
            screen.blit(map1_label, map1_rect)

        # Handle UI interactions
        if mouse_click:
            if state == MAP1 and map1_rect.collidepoint(mouse_pos) and not start_clicked:
                start_clicked = True
                state = COUNTDOWN
            for tower in tower_icons:
                if tower["rect"].collidepoint(mouse_pos) and currency >= tower["cost"]:
                    dragging_tower = True
                    dragged_tower_color = tower["color"]
                    dragged_tower_cost = tower["cost"]
            if pause_rect.collidepoint(mouse_pos):
                previous_state = state
                state = PAUSE

        if dragging_tower and not pygame.mouse.get_pressed()[0]:
            if mouse_pos[1] < screen_height - 100:
                placed_towers.append({"color": dragged_tower_color, "pos": mouse_pos, "cooldown": 0, "range": 150, "rate": 60})
                currency -= dragged_tower_cost
            dragging_tower = False
            dragged_tower_color = None
            dragged_tower_cost = 0

        for tower in placed_towers:
            pygame.draw.circle(screen, tower["color"], tower["pos"], 20)

        if dragging_tower and dragged_tower_color:
            pygame.draw.circle(screen, dragged_tower_color, mouse_pos, 20)

        # Countdown timer visual only (state COUNTDOWN does not interrupt gameplay)
        if state == COUNTDOWN:
            countdown = menu_font.render(str(3), True, (255, 255, 255))
            rect = countdown.get_rect(center=(screen_width // 2, 100))
            screen.blit(countdown, rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            state = WAVE
            continue

        # Enemy logic and tower firing logic
        if state == WAVE and not enemies:
            enemies.append(Enemy(enemy_path))

        for enemy in enemies:
            enemy.move()
            enemy.draw(screen)

        for tower in placed_towers:
            tower["cooldown"] -= 1
            for enemy in enemies:
                dx = tower["pos"][0] - enemy.pos[0]
                dy = tower["pos"][1] - enemy.pos[1]
                dist = (dx**2 + dy**2) ** 0.5
                if dist < tower["range"] and tower["cooldown"] <= 0:
                    enemy.hp -= 10
                    tower["cooldown"] = tower["rate"]
                    pygame.draw.line(screen, (255, 0, 0), tower["pos"], enemy.pos, 2)
                    break

        enemies = [e for e in enemies if e.hp > 0]

        just_entered_map = False

    elif state == MAP2 or state == MAP3:
        screen.fill((100, 0, 0))
        label = map_font.render(f"{state} START", True, (255, 255, 255))
        screen.blit(label, (screen_width // 2 - label.get_width() // 2, screen_height // 2))
        pause_rect = draw_pause_button()
        if mouse_click and pause_rect.collidepoint(mouse_pos):
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
                start_clicked = False
                state = MENU

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
