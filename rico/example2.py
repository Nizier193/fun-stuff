import numpy as np
from random import randint as rand
from functions import *

borders = (1000, 1000)
game = Game(borders, borders=True, fps=60, game_color=(0, 0, 0))
font = pg.font.SysFont('Arial', 25)

# Количество отскоков от стен.
n_bounce = 1
x_lim = 5

# Объекты.
#ed1 = game.create_dot((500, 500), vector=(-5, 0))


ed1 = game.create_dot((400, 400), vector=(rand(-0, 0), rand(-0, 0)))
ed2 = game.create_dot((600, 400), vector=(rand(-0, 0), rand(-0, 0)))

ed3 = game.create_dot((600, 600), vector=(rand(-0, 0), rand(-0, 0)))
ed4 = game.create_dot((200, 600), vector=(rand(-0, 0), rand(-0, 0)))

ed5 = game.create_dot((400, 800), vector=(rand(-0, 0), rand(-0, 0)))


point = game.create_dot((500, 500), (5, 0))

# Вспомогательный модуль подсчёта.
ray_tracer = Ray_Tracer(1000, 1000)

def show_m():
    # Рандомная функция для работы.
    # В целом можно написать абсолютно что угодно.

    mouse_pos = pg.mouse.get_pos()

    # epos1 = ray_trace(ed1.rect.topleft, mouse_pos, 0, ray_tracer, game)
    # epos2 = ray_trace(ed2.rect.topleft, mouse_pos, 0, ray_tracer, game)
    # epos3 = ray_trace(ed3.rect.topleft, mouse_pos, 0, ray_tracer, game)
    # epos4 = ray_trace(ed4.rect.topleft, mouse_pos, 0, ray_tracer, game)
    # epos5 = ray_trace(ed5.rect.topleft, mouse_pos, 0, ray_tracer, game)

    epos1 = ray_trace(ed1.rect.topleft, mouse_pos, ray_tracer, game)
    epos2 = ray_trace(ed2.rect.topleft, mouse_pos, ray_tracer, game)
    epos3 = ray_trace(ed3.rect.topleft, mouse_pos, ray_tracer, game)
    epos4 = ray_trace(ed4.rect.topleft, mouse_pos, ray_tracer, game)
    epos5 = ray_trace(ed5.rect.topleft, mouse_pos, ray_tracer, game)

    pairs = [[epos1, epos2], [epos2, epos3], [epos3, epos5], [epos5, epos4], [epos4, epos1]]

    for i in range(1, 200):
        for pair in pairs:
            epos1 = pair[0]
            epos2 = pair[1]

            xpos1 = ((epos1[0][0] - epos1[2][0]) / (i * 0.5)) + epos1[2][0]
            ypos1 = ((epos1[0][1] - epos1[2][1]) / (i * 0.5)) + epos1[2][1]

            xpos2 = ((epos2[0][0] - epos2[2][0]) / (i * 0.5)) + epos2[2][0]
            ypos2 = ((epos2[0][1] - epos2[2][1]) / (i * 0.5)) + epos2[2][1]

            game.create_line((xpos1, ypos1), (xpos2, ypos2), col=(255 // 200 * (200 - i), 255 // 200 * (200 - i), 255 // 200 * (200 - 0.5 * i)))


    s = 0
    for sprite in game.spr:
        topleft = sprite.rect.center

        dst = round(np.sqrt(np.power(topleft[0] - mouse_pos[0], 2) + np.power(topleft[1] - mouse_pos[1], 2)))
        text = font.render(f'', False, (200, 200, 200))
        game.screen.blit(text, abs(np.array(topleft) + np.array(mouse_pos)) / 2)

        s += dst

    text = font.render(f'{round(s)}', False, (255, 255, 255))
    game.screen.blit(text, (20, 20))

    text = font.render(f'Euclidian dist.', False, (255, 255, 255))
    game.screen.blit(text, (20, 50))

s = 1
def custom():
    grid(50, 1000, 1000, game, showaxis=False)
    def circle_P(point):
        if point.rect.x > 900:
            point.rect.x -= 10
            point.upd_vector((0, s))
        if point.rect.y > 900:
            point.rect.y -= 10
            point.upd_vector((-s, 0))
        if point.rect.x < 100:
            point.rect.x += 10
            point.upd_vector((0, -s))
        if point.rect.y < 100:
            point.rect.y += 10
            point.upd_vector((s, 0))

    circle_P(point)
    circle_P(ed1)
    show_m()

game.custom = lambda: custom()

game.run()
