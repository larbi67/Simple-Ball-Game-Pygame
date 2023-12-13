import pygame
import random

# Initializing Pygame
pygame.init()

# Window Dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football Game LEAD Morocco")

# Loading the background image
background = pygame.image.load("background.png")  # Make sure "background.png" is in the same directory as your script

# Loading the icon image
icon = pygame.image.load("icon.png")  # Replace "icon.png" with your icon image name

# Setting the window icon
pygame.display.set_icon(icon)  # The image should be in ICO or PNG format, size 32x32 or 64x64 pixels

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)
CYAN = (0, 255, 255)
TURQUOISE = (64, 224, 208)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)

# Player
player_width, player_height = 100, 20
player_x, player_y = (WIDTH - player_width) // 2, HEIGHT - player_height - 20
player_speed = 0.1 # adjust to 2 for fast or 1 for slow

# Ball
ball_width, ball_height = 20, 20
ball_x, ball_y = random.randint(0, WIDTH - ball_width), HEIGHT // 2
ball_speed_x, ball_speed_y = 0.1, 0.1  # Reduced speed for a slower game adjust to 2 for fast or 1 for slow

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball bounces off edges
    if ball_x <= 0 or ball_x >= WIDTH - ball_width:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1

    # Collision of the ball with the player
    if player_x <= ball_x <= player_x + player_width and player_y <= ball_y <= player_y + player_height:
        ball_speed_y *= -1
        score += 1

    # Resetting the ball if lost
    if ball_y >= HEIGHT:
        ball_x, ball_y = random.randint(0, WIDTH - ball_width), HEIGHT // 2
        ball_speed_x, ball_speed_y = 0.1, 0.1  # Resetting the speed adjust to 2 for fast or 1 for slow
        score -= 1

    # Displaying the background
    win.blit(background, (0, 0))

    # Displaying the player
    pygame.draw.rect(win, GREEN, (player_x, player_y, player_width, player_height))

    # Displaying the ball
    pygame.draw.ellipse(win, RED, (ball_x, ball_y, ball_width, ball_height))

    # Displaying the score
    text = font.render("Score: " + str(score), True, BLUE)
    win.blit(text, (10, 10))

    pygame.display.update()

# Closing Pygame
pygame.quit()
