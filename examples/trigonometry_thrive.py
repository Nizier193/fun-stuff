from drive.game_drive import Game, dots
from drive.classes import CircularDot, Dot
import math
import pygame as pg


class Config:
    w = 1000
    h = 1000


game = Game((Config.w, Config.h),
            game_color=(0, 0, 0),
            connect_lines=True,
            fps=60
            )

def makecircle(center, radius, steps, pi, letter):
    return CircularDot(
        pos=center,
        startpos=(center[0] + radius, center[1]),
        steps=steps,
        delta_pi=pi,
        letter=letter
    )

center = Dot(velocity=(0, 0), pos=(Config.w / 2, Config.h / 2))
c_1 = CircularDot(
    pos=(Config.w / 2, Config.h / 2),
    startpos=(700, 400),
    steps=2000,
    letter='B'
)
c_2 = CircularDot(
    pos=(Config.w / 2, Config.h / 2),
    startpos=(700, 400),
    steps=2000,
    letter='B',
    delta_pi=math.pi
)
CircularDot(
    pos=(Config.w / 2, Config.h / 2),
    startpos=(700, 400),
    steps=2000,
    letter='B',
    delta_pi = math.pi * 1.5
)
CircularDot(
    pos=(Config.w / 2, Config.h / 2),
    startpos=(700, 400),
    steps=2000,
    letter='B',
    delta_pi=math.pi / 2
)
p_1 = CircularDot(
    pos=(Config.w / 2, Config.h / 2),
    startpos=(600, 400),
    steps=1600,
    letter='B'
)
p_2 = CircularDot(
    pos=(Config.w / 2, Config.h / 2),
    startpos=(600, 400),
    steps=1600,
    letter='B',
    delta_pi=math.pi
)

s_1 = makecircle(tuple(c_1.rect.center), 50, 500, 0, 'C')
s_2 = makecircle(tuple(c_2.rect.center), 50, 500, math.pi, 'C')
l_1 = makecircle((Config.w / 2, Config.h / 2), 1000, 5000, math.pi * 1.5, 'C')
l_2 = makecircle((Config.w / 2, Config.h / 2), 1000, 5000, math.pi / 2, 'C')

game.spr = dots.sprites()
game.connecting_conf = ["AB"]

vel = 0
def custom():
    s_1.cpos = pg.Vector2(c_1.rect.center)
    s_2.cpos = pg.Vector2(c_2.rect.center)
    pg.draw.circle(game.screen, center = (Config.w / 2, Config.h / 2), radius=300, color = (200, 200, 200), width=1)

    pg.draw.circle(game.screen, center=(s_1.rect.center), radius=100, color=(200, 200, 200), width=1)
    pg.draw.circle(game.screen, center=(s_2.rect.center), radius=100, color=(200, 200, 200), width=1)

    pg.draw.circle(game.screen, center=(c_1.rect.center), radius=100, color=(200, 200, 200), width=1)
    pg.draw.circle(game.screen, center=(c_2.rect.center), radius=100, color=(200, 200, 200), width=1)
    pg.draw.circle(game.screen, center=(c_1.rect.center), radius=500, color=(200, 200, 200), width=3)
    pg.draw.circle(game.screen, center=(c_2.rect.center), radius=500, color=(200, 200, 200), width=3)

    pg.draw.circle(game.screen, center=(l_1.rect.center), radius=1000, color=(200, 200, 200), width=2)
    pg.draw.circle(game.screen, center=(l_2.rect.center), radius=1000, color=(200, 200, 200), width=2)



game.custom = custom
game.run()
