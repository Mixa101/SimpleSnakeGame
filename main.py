import pygame
import time
import random

pygame.init()

WIDTH = 400
HEIGHT = 400
CELL_SIZE = 50
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

game_over = False
game_start = False

snake_block = 50
x1 = WIDTH // 2
y1 = HEIGHT // 2
x1_change = 0
y1_change = 0

foodx = round(random.randrange(0, GRID_WIDTH - 1)) * CELL_SIZE
foody = round(random.randrange(0, GRID_HEIGHT - 1)) * CELL_SIZE

pre_key = None

snake_list = []
len_of_snake = 1

font_style = pygame.font.SysFont(None, 50)
small_font_style = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (128, 128, 128), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (128, 128, 128), (0, y), (WIDTH, y))

def change_direction(key, pre_key):
    global x1_change, y1_change
    if key == pygame.K_LEFT and pre_key != pygame.K_RIGHT:
        x1_change = -CELL_SIZE
        y1_change = 0
    elif key == pygame.K_RIGHT and pre_key != pygame.K_LEFT:
        x1_change = CELL_SIZE
        y1_change = 0
    elif key == pygame.K_UP and pre_key != pygame.K_DOWN:
        y1_change = -CELL_SIZE
        x1_change = 0
    elif key == pygame.K_DOWN and pre_key != pygame.K_UP:
        y1_change = CELL_SIZE
        x1_change = 0

def show_start_screen():
    screen.fill((255, 255, 255))
    start_text = font_style.render("Snake Game", True, (0, 0, 0))
    start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(start_text, start_text_rect)

    instruct_text = small_font_style.render("Press SPACE to start", True, (0, 0, 0))
    instruct_text_rect = instruct_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(instruct_text, instruct_text_rect)

def show_game_over_screen():
    screen.fill((255, 255, 255))
    message("You lost", (53, 53, 53))
    pygame.display.update()
    time.sleep(2)

def update_snake():
    x1 += x1_change
    y1 += y1_change

    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
        game_over = True

    screen.fill((255, 255, 255))

    draw_grid()

    pygame.draw.rect(screen, (0, 0, 0), [foodx, foody, CELL_SIZE, CELL_SIZE])

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > len_of_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    for segment in snake_list:
        pygame.draw.rect(screen, (0, 0, 0), [segment[0], segment[1], snake_block, snake_block])

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        print("Yummy!!")
        foodx = round(random.randrange(0, GRID_WIDTH - 1)) * CELL_SIZE
        foody = round(random.randrange(0, GRID_HEIGHT - 1)) * CELL_SIZE
        len_of_snake += 1
        print(f"[ log ] foody = {foody} \t foodx = {foodx},\t len of snake = {len_of_snake}")

    clock.tick(10)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH // 2 - mesg.get_width() // 2, HEIGHT // 2 - mesg.get_height() // 2])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_start = True
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                change_direction(event.key, pre_key)
                pre_key = event.key

    if not game_start:
        show_start_screen()
    else:
        update_snake()

message("You lost", (53, 53, 53))
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
