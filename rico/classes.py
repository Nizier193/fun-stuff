import random
import pygame as pg
import math

dots = pg.sprite.Group()
circulardots = pg.sprite.Group()
blocks = pg.sprite.Group()
class Dot(pg.sprite.Sprite):
    def __init__(self, pos, static = False, letter = 'A'):
        super(Dot, self).__init__()
        self.add(dots)

        self.image = pg.Surface((5, 5))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect(topleft = pos)

        self.letter = letter
        self.static = static
        self.trail = [[self.rect.x, self.rect.y]]
        self.c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

        self.vector = pg.Vector2(
            random.randint(5, 5), random.randint(5, 5)
        )

    def update(self, surface):

        for block in pg.sprite.spritecollide(self, blocks, False):
            if block.type == 'BOTTOM':
                self.trail.append([self.rect.x, self.rect.y])
                self.vector.y *= -1

            if block.type == 'SIDES':
                self.trail.append([self.rect.x, self.rect.y])
                self.vector.x *= -1

        if not self.static:
            self.rect.x += self.vector.x
            self.rect.y += self.vector.y

class CircularDot(pg.sprite.Sprite):
    def __init__(self, pos, radius, inverted):
        super(CircularDot, self).__init__()
        self.add(circulardots)

        self.image = pg.Surface((2, 2))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect(topleft = pos)

        self.cpos = pos
        self.c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

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

    def updatepos(self, index):
        self.rect.x = self.coordinates[index][0]
        self.rect.y = self.coordinates[index][1]

    def update(self):
        if self.index < len(self.coordinates) - 1:
            self.index += 1
        else:
            self.radius += 1
            self.index = 0

        self.updatepos(self.index)

class Block(pg.sprite.Sprite):
    def __init__(self, pos, size, type):
        super(Block, self).__init__()
        self.add(blocks)

        self.image = pg.Surface((size[0], size[1]))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect(topleft = pos)

        self.type = type

class Timer():
    def __init__(self, delay, times):
        self.delay = delay
        self.tick = 0

        self.times_expected = times
        self.times = 0

    def certain_times(self, func):
        if self.times <= self.times_expected:
            func()
            self.times += 1

    def update(self, func):
        self.tick += 1
        if self.tick % self.delay == 0:
            self.certain_times(func)