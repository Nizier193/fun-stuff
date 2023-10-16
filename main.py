import pygame as pg
import math
import random

class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1280, 1000))
        self.clock = pg.time.Clock()

        self.summon(500, (500, 500))
        self.c = 0

    def summon(self, particles, pos):
        for i in range(20, particles, 1):
            Dot(pos, i, False)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            pg.display.update()
            self.screen.fill((0, 0, 0))

            dots.update()
            dots.draw(self.screen)

            if self.c == 1200 or self.c == 2400:
                self.summon(1000, (500, 500))

            self.c += 1

            self.clock.tick(240)

dots = pg.sprite.Group()
class Dot(pg.sprite.Sprite):
    def __init__(self, pos, radius, inverted):
        super(Dot, self).__init__()
        self.add(dots)

        self.image = pg.Surface((5, 5))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect(topleft = pos)

        self.cpos = pos

        self.index = 0
        self.radius = radius
        self.posxs = [x for x in range(self.cpos[0] - radius, self.cpos[0] + radius) if x % 3 == 0]
        self.posxs.append(self.posxs[-1] + 1)

        if inverted:
            coordinates_p = [
                (x, abs(math.sqrt( pow(self.radius, 2) - pow(x - self.cpos[0], 2) ) + self.cpos[1])) for x in self.posxs
            ]
            coordinates_m = [
                (x, abs(math.sqrt(pow(self.radius, 2) - pow(x - self.cpos[0], 2)) - self.cpos[1])) for x in list(reversed(self.posxs))
            ]
        else:
            coordinates_p = [
                (x, abs(math.sqrt( pow(self.radius, 2) - pow(x - self.cpos[0], 2) ) - self.cpos[1])) for x in self.posxs
            ]
            coordinates_m = [
                (x, abs(math.sqrt(pow(self.radius, 2) - pow(x - self.cpos[0], 2)) + self.cpos[1])) for x in list(reversed(self.posxs))
            ]
        self.coordinates = coordinates_p + coordinates_m
    def huyna(self):
        choice = random.choice([True, False])
        if choice:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(100)

    def updatepos(self, index):
        self.rect.x = self.coordinates[index][0]
        self.rect.y = self.coordinates[index][1]

    def update(self):
        if self.index < len(self.coordinates) - 1:
            self.index += 1
        else:
            self.radius += 1
            self.index = 0

        if self.index % 60 == 0:
            self.huyna()

        self.updatepos(self.index)

game = Game()
game.run()