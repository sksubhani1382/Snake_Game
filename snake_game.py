import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1000,800
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Game variables
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Initialize the clock for controlling the frame rate
clock = pygame.time.Clock()

# Set fonts for displaying the score and messages
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, YELLOW)
    game_window.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, BLACK, [x[0], x[1], snake_block, snake_block])


def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_window.fill(BLUE)
            display_message("You Lost! Press C-Play Again or Q-Quit", RED)
            display_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # Check for boundaries
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_window.fill(BLUE)
        pygame.draw.rect(game_window, GREEN, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_List)
        display_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


# Start the game
game_loop()