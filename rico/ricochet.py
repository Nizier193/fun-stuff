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

        self.spr.append(Dot((350, 250),  False, 'A'))
        self.spr.append(Dot((550, 250),  False, 'B'))
        self.spr.append(Dot((350, 450),  False, 'C'))
        self.spr.append(Dot((550, 450),  False, 'D'))

        self.spr.append(Dot((450, 350),  True, 'E'))
        self.spr.append(Dot((650, 350),  True, 'F'))
        self.spr.append(Dot((450, 550),  True, 'G'))
        self.spr.append(Dot((650, 550),  True, 'H'))

        self.connecting_conf = ['AB', 'AC', 'CD', 'BD', 'AE', 'BF', 'CG', 'DH', 'EG', 'GH', 'HF', 'FE']

        self.create_box((-5, -5), 1005, 5)

        self.timer = Timer(80, 2)

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
    connect_lines=True
)
game.run()
