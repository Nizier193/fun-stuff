import pygame as pg
import math
import random
import json
from classes import *

class Game():
    def __init__(self, connect_lines = True, trails_lines = False, pre_loaded_asset = False):
        pg.init()
        self.screen = pg.display.set_mode((1000, 1000))
        self.clock = pg.time.Clock()

        self.connect_lines = connect_lines
        self.trails_lines = trails_lines

        self.spr = []
        self.asset = json.load(open('config.json')) if pre_loaded_asset else None

        self.connecting_conf = self.create_cube(pg.Vector2(160, 80))
        self.trailed_conf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        self.create_box((50, 50), 500, 20)

        self.timer1 = Timer(100, 0)
        self.timer2 = Timer(200, 1)

        class Letter():
            def __init__(self):
                pass
        self.letter = Letter

    def create_dot(self, topleft, static, letter, vector):
        self.spr.append(Dot((topleft.x, topleft.y),  pg.Vector2(
            vector[0], vector[1]
        ), static, letter))

    def create_cube(self, topleft, static = False, rnd = [3, 5]):
        ltrs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        for ltr, asset in zip(ltrs, self.asset if self.asset != None else rnd):
            self.create_dot(topleft, static, ltr, asset)

        lst = [[body.vector.x, body.vector.y] for body in self.spr]
        file = open('config.json', 'w', encoding='UTF-8').write(str(lst))

        connections = ['AB', 'AC', 'CD', 'BD', 'AE', 'BF', 'CG', 'DH', 'EG', 'GH', 'HF', 'FE']

        return [f'{ltr1}{ltr2}' for ltr1 in ltrs for ltr2 in ltrs]

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
    trails_lines=False,
    connect_lines=True,
    pre_loaded_asset=True
)
game.run()
