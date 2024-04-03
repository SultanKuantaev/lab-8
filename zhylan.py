import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Настройки змеи
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]
food_pos = [0, 0]
food_spawn = True
score = 0
level = 1
speed_increase = 0.1  # Увеличение скорости за уровень

# Контроллер FPS
fps = pygame.time.Clock()

def check_collision(pos):
    # Проверка столкновения змеи с границами
    if pos[0] < 0 or pos[0] > SCREEN_WIDTH-10 or pos[1] < 0 or pos[1] > SCREEN_HEIGHT-10:
        return True
    # Проверка столкновения змеи с самой собой
    if pos in snake_pos[1:]:
        return True
    return False

def get_random_position():
    # Генерация позиции еды, не на змее и не на стенах
    while True:
        pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
        if pos not in snake_pos:
            return pos

# Главный цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Управление движением змеи
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_speed[1] == 0:
                snake_speed = [0, -10]
            elif event.key == pygame.K_DOWN and snake_speed[1] == 0:
                snake_speed = [0, 10]
            elif event.key == pygame.K_LEFT and snake_speed[0] == 0:
                snake_speed = [-10, 0]
            elif event.key == pygame.K_RIGHT and snake_speed[0] == 0:
                snake_speed = [10, 0]

    snake_pos.insert(0, list(map(lambda x, y: x + y, snake_pos[0], snake_speed)))

    # Проверка на столкновение с границами или самим собой
    if check_collision(snake_pos[0]):
        pygame.quit()
        sys.exit()

    # Проверка, съела ли змея еду
    if snake_pos[0] == food_pos:
        score += 1
        food_spawn = True
    else:
        snake_pos.pop()

    if food_spawn:
        food_pos = get_random_position()
        food_spawn = False

    # Обновление скорости игры и уровня в зависимости от счета
    if score == (level * 3):  # Следующий уровень каждые 3 еды
        level += 1
        fps.tick(10 + level*speed_increase)  # Увеличение скорости игры

    screen.fill(BLACK)

    # Рисование змеи
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Рисование еды
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Отображение счета и уровня
    font = pygame.font.SysFont('arial', 20)
    score_text = font.render("Счет: " + str(score) + " Уровень: " + str(level), True, WHITE)
    screen.blit(score_text, [0, 0])

    pygame.display.flip()
    fps.tick(10 + level*speed_increase)  # Контроль скорости игры
