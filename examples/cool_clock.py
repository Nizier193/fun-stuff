import random
import pygame as pg

from drive.classes import CircularDot
from drive.game_drive import Ray_Tracer, Game
from drive.functions import grid

borders = (1000, 1000)
game = Game(borders, borders=True, fps=60, game_color=(0, 0, 0))
font = pg.font.SysFont('Arial', 50)

f1 = CircularDot((500, 500), 50, inverted=True)
f2 = CircularDot((500, 500), 200, inverted=True)
f3 = CircularDot((500, 500), 450, inverted=True)

f4 = CircularDot(f1.rect.center, 50, inverted=True)
f4.body = f1

r_t = Ray_Tracer(1000, 1000)


counter = 0
text = font.render(f'{random.randint(10, 100)}', False, (255, 255, 255))
text2 = font.render(f'{random.randint(10, 100)}', False, (255, 255, 255))
split = font.render(f':', False, (255, 255, 255))
def custom():
    global counter, text, text2

    grid(50, 1000, 1000, game, showaxis=False)

    pg.draw.circle(game.screen, (255, 255, 255), (500, 500), 200, width=2)
    pg.draw.circle(game.screen, (100, 100, 100), (500, 500), 50, width=2)
    pg.draw.circle(game.screen, (200, 200, 200), (500, 500), 450, width=2)

    pg.draw.circle(game.screen, (255, 255, 255), f1.rect.center, 50, width=1)
    pg.draw.circle(game.screen, (255, 255, 255), f2.rect.center, 100, width=1)
    pg.draw.circle(game.screen, (255, 255, 255), f3.rect.center, 150, width=1)

    game.create_line((500, 500), f1.rect.center, col = (255, 255, 255))
    game.create_line((500, 500), f2.rect.center, col = (255, 255, 255))
    game.create_line((500, 500), f3.rect.center, col = (255, 255, 255))
    game.create_line(f1.rect.center, f4.rect.center, col = (255, 255, 255))

    if counter % 30 == 0:
        text = font.render(f'{random.randint(10, 99)}', False, (255, 255, 255))
        text2 = font.render(f'{random.randint(10, 99)}', False, (255, 255, 255))

    game.screen.blit(text, (445, 200))
    game.screen.blit(split, (500, 200))
    game.screen.blit(text2, (525, 200))

    counter += 1

game.custom = lambda: custom()

game.run()
