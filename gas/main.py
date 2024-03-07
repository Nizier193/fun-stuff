import pygame as pg
import math
import random
from classes import *


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((map_size[0], map_size[1]))
        self.clock = pg.time.Clock()

        self.my_font = pg.font.SysFont('Comic Sans MS', 30)

        for i in range(100):
            Molecule()

    def calc_kinetic(self):
        sum = 0
        for mol in molecules:
            sum += mol.velocity.x + mol.velocity.y

        return sum

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            pg.display.update()
            self.screen.fill((0, 0, 0))

            font = self.my_font.render(str(self.calc_kinetic()), False, (255, 255, 255))
            self.screen.blit(font, (20, 20))

            molecules.update()
            molecules.draw(self.screen)

            self.clock.tick(60)


game = Game()
game.run()
