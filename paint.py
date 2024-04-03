import pygame
#p - обычный s - circles c - rectanglge e - eraser r g b - для цветов
def main():
    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    # Радиус круга и начальная позиция
    radius = 15
    x = 0
    y = 0
    color = (0, 0, 255)  # Начальный цвет - синий
    mode = 'draw'  # Начальный режим - рисование

    # Инициализация рисования и начальная позиция
    drawing = False
    start_pos = None

    while True:
        
        pressed = pygame.key.get_pressed()

        # Проверка на зажатие клавиш Alt или Ctrl
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # Выход при закрытии окна или использовании сочетаний клавиш
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Выбор цвета
                if event.key == pygame.K_r:
                    color = (255, 0, 0)  # Красный
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)  # Зеленый
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)  # Синий
                
                # Выбор режима
                if event.key == pygame.K_d:
                    mode = 'draw'  # Рисование
                elif event.key == pygame.K_c:
                    mode = 'circle'  # Круг
                elif event.key == pygame.K_s:
                    mode = 'square'  # Квадрат
                elif event.key == pygame.K_e:
                    mode = 'erase'  # Ластик
                elif event.key == pygame.K_p:
                    mode = 'pencil'  # Карандаш (обычный режим)

            # Изменение размера радиуса круга
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Левая кнопка мыши
                    if mode in ['circle', 'square']:
                        start_pos = event.pos
                    else:
                        drawing = True
                elif event.button == 3: # Правая кнопка мыши
                    if mode == 'erase':
                        radius = max(1, radius - 1)
                pygame.display.flip()

            elif event.type == pygame.MOUSEBUTTONUP:
                if mode in ['circle', 'square']:
                    end_pos = event.pos
                    if mode == 'circle':
                        pygame.draw.circle(screen, color, start_pos, radius)
                    elif mode == 'square':
                        rect_width = end_pos[0] - start_pos[0]
                        rect_height = end_pos[1] - start_pos[1]
                        pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], rect_width, rect_height))
                    pygame.display.flip()
                else:
                    drawing = False

            # Рисование или стирание в зависимости от режима
            if event.type == pygame.MOUSEMOTION:
                if mode == 'erase':
                    if drawing:
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)
                        pygame.display.flip()
                elif mode == 'pencil':
                    if drawing:
                        end_pos = event.pos
                        pygame.draw.line(screen, color, start_pos, end_pos, radius)
                        start_pos = end_pos
                        pygame.display.flip()

        clock.tick(60)

main()
