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

        self.image = pg.Surface((2, 2))
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
    def __init__(self, pos, startpos, steps=50, delta_pi=0, letter='A'):
        super(CircularDot, self).__init__()
        self.add(dots)

        self.image = pg.Surface((2, 2))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect(center = pos)

        self.trail = [[self.rect.x, self.rect.y]]
        self.cpos = pg.Vector2(pos)
        self.startpos = startpos
        self.steps = steps
        self.c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.letter = letter
        self.index = 0

        self.timer = Timer(13, 100)
        self.delta_pi = delta_pi

        delta_x = self.startpos[0] - self.cpos.x
        delta_y = self.startpos[1] - self.cpos.y
        self.vector = pg.Vector2((delta_x, delta_y)).length()

    def trigonometry_calc(self, delta_pi) -> list[list]:
        '''
        Split circumsphere to equal then calc the positions
        :return: Pos
        '''

        # try: delta_pi = math.asin(delta_x / delta_y)
        # except Exception as e: delta_pi = math.pi if delta_x < 0 else 0; print(e)

        posx = [math.cos(math.pi * 2 / self.steps * n + delta_pi) * self.vector for n in range(1, self.steps + 1)]
        posy = [math.sin(math.pi * 2 / self.steps * n + delta_pi) * self.vector for n in range(1, self.steps + 1)]

        return [[x, y] for x, y in zip(posx, posy)]

    def update(self, surface):
        self.pos = self.trigonometry_calc(self.delta_pi)

        self.rect.centerx = self.pos[self.index][0] + self.cpos.x
        self.rect.centery = self.pos[self.index][1] + self.cpos.y

        self.index += 1

        self.index = 0 if self.index >= self.steps else self.index



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

