import pygame as pg
import math
import random
from classes import *

class Game():
    def __init__(self, connect_lines = True, trails_lines = False):
        pg.init()
        self.screen = pg.display.set_mode((1000, 1000))
        self.clock = pg.time.Clock()

        self.connect_lines = connect_lines
        self.trails_lines = trails_lines

        self.spr = []

        self.spr.append(CircularDot((500, 500), 50, False, 'A'))

        self.connecting_conf = self.create_cube(pg.Vector2(20, 10), 200, False)
        self.trailed_conf = ['A', 'B']

        self.create_box((-5, -5), 1005, 5)

        self.timer1 = Timer(100, 0)
        self.timer2 = Timer(200, 0)

        class Letter():
            def __init__(self):
                pass
        self.letter = Letter

    def create_cube(self, topleft, size, static = False):
        self.spr.append(Dot((topleft.x, topleft.y),  pg.Vector2(
            random.randint(4, 4), random.randint(5, 5)
        ), static, 'A'))
        self.spr.append(Dot((topleft.x + size, topleft.y),  pg.Vector2(
            random.randint(4, 4), random.randint(5, 5)
        ),  static, 'B'))
        self.spr.append(Dot((topleft.x, topleft.y + size),  pg.Vector2(
            random.randint(4, 4), random.randint(5, 5)
        ),  static, 'C'))
        self.spr.append(Dot((topleft.x + size, topleft.y + size),  pg.Vector2(
            random.randint(4, 4), random.randint(5, 5)
        ),  static, 'D'))

        self.spr.append(Dot((topleft.x + size / 2, topleft.y + size / 2),  pg.Vector2(
            random.randint(5, 5), random.randint(8, 8)
        ),  static, 'E'))
        self.spr.append(Dot((topleft.x + size + size / 2, topleft.y + size / 2),  pg.Vector2(
            random.randint(5, 5), random.randint(8, 8)
        ),  static, 'F'))
        self.spr.append(Dot((topleft.x + size / 2, topleft.y + size + size / 2),  pg.Vector2(
            random.randint(5, 5), random.randint(8, 8)
        ),  static, 'G'))
        self.spr.append(Dot((topleft.x + size + size / 2, topleft.y + size + size / 2),  pg.Vector2(
            random.randint(5, 5), random.randint(8, 8)
        ), static, 'H'))
        return ['AB', 'AC', 'CD', 'BD', 'AE', 'BF', 'CG', 'DH', 'EG', 'GH', 'HF', 'FE']

    def create_box(self, topleft, size, width):
        Block(topleft, (size, width), 'BOTTOM')
        Block(topleft, (width, size), 'SIDES')
        Block((topleft[0], topleft[1] + size), (size, width), 'BOTTOM')
        Block((topleft[0] + size, topleft[1]), (width, size + width), 'SIDES')

    def connecting_lines(self):
        if self.connect_lines:
            for connected in self.connecting_conf:
                a = connected[0]
                b = connected[1]
                expconnected = list(filter(lambda x: x.letter == a or x.letter == b, self.spr))
                for dot in expconnected:
                    for i in expconnected:
                        if i != dot:
                            pg.draw.line(surface=self.screen, color=dot.c,
                                         start_pos=[dot.rect.x, dot.rect.y],
                                         end_pos=[i.rect.x, i.rect.y])

    def trail_lines(self):
        if self.trails_lines:
            for dot in dots:
                if dot.letter in self.trailed_conf:
                    for index, coords in enumerate(dot.trail):
                        if len(dot.trail) != 1 and index != len(dot.trail) - 1:
                            pg.draw.line(surface=self.screen, color=dot.c,
                                         start_pos=coords,
                                         end_pos=dot.trail[index + 1])

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            pg.display.update()
            self.screen.fill((0, 0, 0))

            dots.update(self.screen)
            dots.draw(self.screen)

            circulardots.update()
            circulardots.draw(self.screen)

            blocks.update()
            blocks.draw(self.screen)

            self.connecting_lines()
            self.trail_lines()

            self.clock.tick(60)

game = Game(
    trails_lines=True,
    connect_lines=True
)
game.run()
