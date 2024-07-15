import json
from drive.classes import *


class Game():
    def __init__(self,
                 size,
                 connect_lines=False,
                 trails_lines=False,
                 pre_loaded_asset=False,
                 borders=False,
                 fps=60,
                 game_color = (200, 200, 200)):
        '''
        :param connect_lines: Соединены ли отображаемые точки между собой.
        :param trails_lines: Оставляют ли следы отображаемые точки при столкновении с блоком.
        :param pre_loaded_asset: Загружается ли уже заранее определенные параметры точек. (config.json)
        spr - список всех объектов классов Dot и CircularDot
        asset - предзагруженные параметры velocity для точек.
        connecting_conf - список с соединениями точек между собой вида ['AB', 'ab']
        trailed_conf - список, определяющий отслеживание точек через их условное обозначение.

        Базовый класс определяющий поведение игры.
        '''
        self.fps = fps
        self.game_color = game_color
        self.borders = borders

        pg.init()
        self.screen = pg.display.set_mode((size))
        self.clock = pg.time.Clock()

        self.connect_lines = connect_lines

        self.trails_lines = trails_lines

        self.spr = []
        self.asset = json.load(open('../config.json')) if pre_loaded_asset else None
        self.connecting_conf = None
        self.trailed_conf = None

    def create_dot(self, topleft, vector = None, letter = None):
        topleft = pg.Vector2(topleft[0], topleft[1])

        dot = Dot((topleft.x, topleft.y), pg.Vector2(
            vector[0], vector[1]
        ), letter)
        dot.brds = self.borders

        self.spr.append(dot)
        return dot

    def create_line(self, pos_start, pos_end, col = (70, 50, 50)):
        pg.draw.line(self.screen, col, pos_start, pos_end)

    def create_cube(self, topleft, static=False, rnd=[3, 5]):
        topleft = pg.Vector2(topleft[0], topleft[1])

        '''
        :param topleft: Положение левого верхнего угла A на плоскости
        :param static: Является ли статичным куб
        :param rnd: Рандомность движения точек
        '''

        ltrs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        if self.asset:
            for ltr, asset in zip(ltrs, self.asset):
                self.create_dot(topleft, static, ltr, asset)
        else:
            for ltr in ltrs:
                self.create_dot(topleft, static, ltr,
                                pg.Vector2(random.randint(rnd[0], rnd[1]), random.randint(rnd[0], rnd[1])))

        connections = ['AB', 'AC', 'CD', 'BD', 'AE', 'BF', 'CG', 'DH', 'EG', 'GH', 'HF', 'FE']

        spr = self.spr

        self.connecting_conf = [f'{ltr1}{ltr2}' for ltr1 in ltrs for ltr2 in ltrs]
        self.vectors = [[body.vector.x, body.vector.y] for body in spr]

        return self.vectors, self.connecting_conf

    def create_circle(self, centerpos, radius, divide=100, delta_pi=0, letter='A'):
        return CircularDot(
            pos=centerpos,
            startpos=(centerpos[0] + radius, centerpos[1]),
            steps=divide,
            delta_pi=delta_pi,
            letter=letter
        )

    def __create_box(self, topleft, size, width):
        topleft = pg.Vector2(topleft[0], topleft[1])

        Block(topleft, (size, width), 'BOTTOM')
        Block(topleft, (width, size), 'SIDES')
        Block((topleft[0], topleft[1] + size), (size, width), 'BOTTOM')
        Block((topleft[0] + size, topleft[1]), (width, size + width), 'SIDES')

    def __connecting_lines(self):
        if self.connect_lines:
            for connected in self.connecting_conf:
                a = connected[0]
                b = connected[1]
                expconnected_a = list(filter(lambda x: x.letter == a, self.spr))
                expconnected_b = list(filter(lambda x: x.letter == b, self.spr))
                for dot in expconnected_a:
                    for i in expconnected_b:
                        if i != dot:
                            pg.draw.line(surface=self.screen, color=dot.c,
                                         start_pos=[dot.rect.x, dot.rect.y],
                                         end_pos=[i.rect.x, i.rect.y])

    def __trail_lines(self):
        if self.trails_lines:
            for dot in dots:
                if dot.letter in self.trailed_conf:
                    for index, coords in enumerate(dot.trail):
                        if len(dot.trail) != 1 and index != len(dot.trail) - 1:
                            pg.draw.line(surface=self.screen, color=dot.c,
                                         start_pos=coords,
                                         end_pos=dot.trail[index + 1])
    def custom(self):
        pass

    def run(self, *args):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            pg.display.update()
            self.screen.fill(self.game_color)

            self.custom()

            dots.update(self.screen)
            dots.draw(self.screen)

            circulardots.update()
            circulardots.draw(self.screen)

            blocks.update()
            blocks.draw(self.screen)

            self.__connecting_lines()
            try:
                self.__trail_lines()
            except Exception:
                raise Exception('Не указан параметр соединения точек -> game.trail_conf; для примера: ["A", "B", "C"]')

            for arg in args:
                try:
                    arg()
                except Exception:
                    pass

            self.clock.tick(self.fps)

class Ray_Tracer():
    def __init__(self, width, height):
        self.width, self.height = width, height

    #                      x_pos       y_pos        x_dest                      y_dest
    # game.create_line((topleft[0], topleft[1]), (topleft[0] + 1000 * sign, topleft[1] + (sign * cf * 1000)))
    def calc(self, coef, x_pos, y_pos, sign, rev=False):

        sw = sign[0] * -1 if rev else sign[0]
        sh = sign[1] * -1 if rev else sign[1]

        w = self.width if sw == -1 else 0
        h = self.height if sh == -1 else 0

        y_dest = coef * (w - x_pos) + y_pos
        if y_dest < self.height and y_dest > 0:
            return w, coef * (w - x_pos) + y_pos, (sw, sh)
        else:
            # ОШИБКА КРОЕТСЯ В ИНВЕРСИИ ЗНАКОВ!
            return ((h - y_pos) / coef) + x_pos, h, (-sw, -sh)