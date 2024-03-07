import numpy as np
from random import randint as rand
from functions import *

borders = (1000, 1000)
game = Game(borders, borders=True, fps=60)
font = pg.font.SysFont('Arial', 25)

# Количество отскоков от стен.
n_bounce = 100

# Объекты.
example_dot = game.create_dot((300, 300), vector=(rand(-5, 5), rand(-5, 5)))

# Вспомогательный модуль подсчёта.
ray_tracer = Ray_Tracer(1000, 1000)

def show_m():
    # Рандомная функция для работы.
    # В целом можно написать абсолютно что угодно.

    mouse_pos = pg.mouse.get_pos()

    s = 0
    for sprite in game.spr:
        topleft = sprite.rect.center
        info = ray_trace(mouse_pos, topleft, n_bounce, ray_tracer, game)

        dst = round(np.sqrt(np.power(topleft[0] - mouse_pos[0], 2) + np.power(topleft[1] - mouse_pos[1], 2)), 6)
        text = font.render(f'{info}', False, (200, 200, 200))
        game.screen.blit(text, abs(np.array(topleft) + np.array(mouse_pos)) / 2)

        s += dst

    text = font.render(f'{round(s)}', False, (255, 255, 255))
    game.screen.blit(text, (20, 20))

    text = font.render(f'Euclidian dist.', False, (255, 255, 255))
    game.screen.blit(text, (20, 50))

def custom():
    grid(50, 1000, 1000, game, showaxis=True)
    show_m()

game.custom = lambda: custom()

game.run()
