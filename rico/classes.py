import random
import pygame as pg
import math

dots = pg.sprite.Group()
circulardots = pg.sprite.Group()
blocks = pg.sprite.Group()
class Dot(pg.sprite.Sprite):
    '''
    Класс, объекты которого являются точки со способностью к отскакиванию от стен классов Block или от границ
    окна, если флаг borders == True.
    '''
    def __init__(self, pos, velocity, letter = 'A'):
        '''
        :param pos: Положение точки на координатной плоскости.
        :param velocity: Начальная скорость точки.
        :param static: Статична ли точка.
        :param letter: Условное обозначение точки. Используется при отслеживании траектории или соединения точек между собой.

        trail - атрибут для отслеживания траектории.
        '''
        super(Dot, self).__init__()
        self.add(dots)

        self.image = pg.Surface((5, 5))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect(topleft = pos)

        self.brds = False
        self.letter = letter
        self.trail = [[self.rect.x, self.rect.y]]
        self.c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

        self.vector = pg.Vector2(velocity[0], velocity[1])

    def borders(self):
        if self.brds:
            scr = pg.display.get_window_size()
            if self.rect.x > scr[0]:
                self.trail.append([self.rect.x, self.rect.y])
                self.vector.x = -self.vector.x
            if self.rect.x < 0:
                self.trail.append([self.rect.x, self.rect.y])
                self.vector.x = -self.vector.x

            if self.rect.y > scr[1]:
                self.trail.append([self.rect.x, self.rect.y])
                self.vector.y = -self.vector.y
            if self.rect.y < 0:
                self.trail.append([self.rect.x, self.rect.y])
                self.vector.y = -self.vector.y

    def upd_vector(self, new_vector):
        '''
        Allowes you to change dot`s vector with just a simple tuple.
        :param new_vector: tuple
        :return: nothing
        '''

        self.vector = pg.Vector2(new_vector[0], new_vector[1])

    def update(self, surface):
        self.rect.x += self.vector.x
        self.rect.y += self.vector.y

        self.borders()


        for block in pg.sprite.spritecollide(self, blocks, False):
            if block.type == 'BOTTOM':
                self.trail.append([self.rect.x, self.rect.y])
                self.vector.y *= -1

            if block.type == 'SIDES':
                self.trail.append([self.rect.x, self.rect.y])
                self.vector.x *= -1



class CircularDot(pg.sprite.Sprite):
    '''
    Класс, объекты которого являются точками, вращающимися вокруг центра радиусом radius.
    Вращение задано уравнением окружности r^2 = x^2 + y^2

    Траектория задаётся путем включения точки каждые n секунд. n задаётся через объект
    класса Timer.
    '''
    def __init__(self, pos, radius, inverted=False, letter='A'):
        super(CircularDot, self).__init__()
        self.add(dots)

        self.image = pg.Surface((0, 0))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect(topleft = pos)

        self.trail = [[self.rect.x, self.rect.y]]
        self.cpos = pos
        self.c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.letter = letter
        self.index = 0
        self.radius = radius
        self.posxs = [x for x in range(self.cpos[0] - radius, self.cpos[0] + radius)]
        self.posxs.append(self.posxs[-1] + 1)

        #--
        self.body = None
        #--

        self.timer = Timer(13, 100)

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
        x = self.coordinates[index][0]
        y = self.coordinates[index][1]

        self.rect.x, self.rect.y = self.updatepos_corr((x, y), self.body)

    def updatepos_corr(self, curr_pos, body):
        x = body.rect.centerx if body else 0
        y = body.rect.centery if body else 0

        return (curr_pos[0], curr_pos[1])

    def update(self, surface):
        if self.index < len(self.coordinates) - 1:
            self.index += 1
        else:
            self.radius += 1
            self.index = 0

        self.timer.update(lambda: self.trail.append([self.rect.x, self.rect.y]))
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
    '''
    Объект этого класса исполняет какое либо действие каждые delay тиков times раз.
    '''
    def __init__(self, delay, times):
        self.delay = delay
        self.tick = 0

        self.times_expected = times
        self.times = 0

    def certain_times(self, func):
        if self.times <= self.times_expected:
            self.times += 1

            return func()

    def update(self, func):
        self.tick += 1

        if self.tick % self.delay == 0:
            return self.certain_times(func)

