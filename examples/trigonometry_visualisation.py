import pygame as pg

from drive.game_drive import *
from drive.classes import *

class Config:
    width = 1000
    height = 800
    wh = (width, height)

game = Game(
    Config.wh,
    game_color=(0, 0, 0),
    connect_lines=True,
    fps=4800
)
int_ = random.randint(500, 1000)
Dot((400, 400), (0, 0), letter='A')
circle = game.create_circle((400, 400), 150, divide=int(int_ * math.e), letter='B')
circle_2 = game.create_circle(circle.cpos, 100, divide=int(int_ * math.pi), letter='C')
circle_3 = game.create_circle(circle.cpos, 50, divide=int_, letter='D')


game.spr = dots.sprites()
game.connecting_conf = ['AB', 'BC', 'CD']

lines = []

def custom():
    circle_2.cpos = pg.Vector2(circle.rect.center)
    circle_3.cpos = pg.Vector2(circle_2.rect.center)

    lines.append(circle_3.rect.center)
    if len(lines) != 1:
        for index, line in enumerate(lines):
            if index != len(lines) - 1:
                pg.draw.line(game.screen, (200, 200, 200), line, lines[index + 1])

    pass
game.custom = custom
game.run()