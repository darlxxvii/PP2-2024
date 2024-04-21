import pygame
import time
import random

# Инициализация параметров игры
snake_speed = 9
window_x, window_y = 720, 480
pygame.init()
pygame.display.set_caption('Nazerke\'s Snake game')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()
snake_position = [100, 50]
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 204)
pink = (255, 51, 255)
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
direction = 'RIGHT'
change_to = direction
score = 0
level = 1  # Initialize level

# Фрукты с весом и таймером
fruit_positions = [([random.randrange(1, (window_x//10)) * 10,
                     random.randrange(1, (window_y//10)) * 10], random.randint(1, 5), 80)]

# Функция для отображения счета и уровня
def show_score_and_level(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}  Level: {level}', True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Функция для обработки окончания игры
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, pink)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Обновление направления движения змейки
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Обновление позиции головы змейки
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Добавление новой головы в тело змейки
    snake_body.insert(0, list(snake_position))

    # Проверка съедения фрукта
    fruit_eaten = False
    for i, (fruit_position, weight, timer) in enumerate(fruit_positions):
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10 * weight
            fruit_eaten = True
            del fruit_positions[i]
            break

    # Удаление последнего сегмента тела, если фрукт не съеден
    if not fruit_eaten:
        snake_body.pop()
    else:
        # Добавление нового фрукта, если их меньше 4
        if len(fruit_positions) < 4:
            fruit_positions.append(([
                random.randrange(1, (window_x//10)) * 10,
                random.randrange(1, (window_y//10)) * 10
            ], random.randint(1, 5), 10))

    # Обновление таймеров фруктов и удаление фруктов с истекшим таймером
    fruit_positions = [([x, y], w, t - 1) for [x, y], w, t in fruit_positions if t > 0]

    # Заполнение игрового окна черным цветом
    game_window.fill(black)

    # Отрисовка змейки
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Отрисовка фруктов
    for fruit_position, weight, _ in fruit_positions:
        pygame.draw.rect(game_window, red, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

    # Проверка столкновения змейки с границами игрового поля
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Проверка столкновения змейки с собственным телом
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Отображение счета и уровня
    show_score_and_level(pink, 'times new roman', 20)

    # Увеличение уровня и скорости змейки
    if score >= level * 20:
        level += 1
        snake_speed += 1

    # Обновление дисплея и контроль частоты кадров
    pygame.display.update()
    fps.tick(snake_speed)
