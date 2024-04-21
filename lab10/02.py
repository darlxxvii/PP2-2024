import psycopg2
import pygame
import time
import random

# Database connection setup
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="Nnaz9191%", port=5432)
cur = conn.cursor()

# Ensure the database table exists
cur.execute("""
CREATE TABLE IF NOT EXISTS Snake (
    name VARCHAR(255),
    score INT,
    level INT
);
""")

name = input("Enter your name: ")
cur.execute("SELECT (score, level) FROM Snake WHERE name=%s;", (name))
result = cur.fetchone()
if result:
    print(result)
    quit()
# Game initialization
snake_speed = 9
window_x, window_y = 720, 480
pygame.init()
pygame.display.set_caption("Nazerke's Snake game")
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()
snake_position = [100, 50]
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
pink = (255, 51, 255)
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
direction = 'RIGHT'
change_to = direction
score = 0
level = 1

# Fruit setup
fruit_positions = [([random.randrange(1, (window_x//10)) * 10,
                     random.randrange(1, (window_y//10)) * 10], random.randint(1, 5), 120)]

def show_score_and_level():
    score_font = pygame.font.SysFont('times new roman', 20)
    score_surface = score_font.render(f'Score: {score} Level: {level}', True, pink)
    game_window.blit(score_surface, (0, 0))

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Your Score is: {score}', True, pink)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    cur.execute("INSERT INTO Snake (name, score, level) VALUES (%s, %s, %s);", (name, score, level))
    conn.commit()
    
    pygame.quit()
    quit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    if change_to in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
        direction = change_to

    # Update snake position
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    # Fruit eating logic
    fruit_eaten = False
    for i, (fruit_position, weight, timer) in enumerate(fruit_positions):
        if snake_position == fruit_position:
            score += 10 * weight
            fruit_eaten = True
            fruit_positions.pop(i)
            break

    if not fruit_eaten:
        snake_body.pop()

    if len(fruit_positions) < 4:
        fruit_positions.append(([random.randrange(1, (window_x//10)) * 10,
                                 random.randrange(1, (window_y//10)) * 10], random.randint(1, 5), 120))

    game_window.fill(black)

    for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Drawing fruits
    for fruit_position, weight, _ in fruit_positions:
        pygame.draw.rect(game_window, red, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

    # Display score and level on the game window
    show_score_and_level()

    # Check for collisions with the game boundaries
    if snake_position[0] < 0 or snake_position[0] > window_x - 10 or snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Check for collision with itself
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Increasing the level and speed of the snake as the score increases
    if score >= level * 20:
        level += 1
        snake_speed += 1

    # Update the display and control the frame rate
    pygame.display.update()
    fps.tick(snake_speed)

# Close database cursor and connection after the game loop
cur.close()
conn.close()

