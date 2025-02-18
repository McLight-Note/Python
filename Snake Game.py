import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen size
width, height = 600, 400
win = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake settings
block_size = 10
speed = 15

# Fonts
font = pygame.font.SysFont("bahnschrift", 25)

# Function to display score
def show_score(score):
    value = font.render(f"Score: {score}", True, white)
    win.blit(value, [10, 10])

# Main game function
def game():
    game_over = False
    game_close = False

    # Snake position
    x, y = width // 2, height // 2
    x_change, y_change = 0, 0

    # Snake body
    snake = []
    length = 1

    # Food position
    food_x = random.randrange(0, width - block_size, block_size)
    food_y = random.randrange(0, height - block_size, block_size)

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            win.fill(black)
            msg = font.render("Game Over! Press Q-Quit or C-Continue", True, red)
            win.blit(msg, [width // 6, height // 3])
            show_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change, y_change = -block_size, 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change, y_change = block_size, 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change, y_change = 0, -block_size
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change, y_change = 0, block_size

        # Move snake
        x += x_change
        y += y_change

        # Check for collisions
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        win.fill(black)
        pygame.draw.rect(win, green, [food_x, food_y, block_size, block_size])

        snake_head = [x, y]
        snake.append(snake_head)
        if len(snake) > length:
            del snake[0]

        # Check if snake collides with itself
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        for segment in snake:
            pygame.draw.rect(win, blue, [segment[0], segment[1], block_size, block_size])

        show_score(length - 1)
        pygame.display.update()

        # Check if food is eaten
        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - block_size, block_size)
            food_y = random.randrange(0, height - block_size, block_size)
            length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

game()