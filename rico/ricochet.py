import json
from classes import *

class Game():
    def __init__(self, size, connect_lines = False, trails_lines = False, pre_loaded_asset = False, borders = False, fps = 60):
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
        self.borders = borders

        pg.init()
        self.screen = pg.display.set_mode((size))
        self.clock = pg.time.Clock()

        self.connect_lines = connect_lines
        self.trails_lines = trails_lines

        self.spr = []
        self.asset = json.load(open('config.json')) if pre_loaded_asset else None
        self.connecting_conf = None
        self.trailed_conf = None


    def create_dot(self, topleft, static, letter, vector):
        dot = Dot((topleft.x, topleft.y),  pg.Vector2(
            vector[0], vector[1]
        ), static, letter)
        dot.brds = self.borders

        self.spr.append(dot)
        return dot

    def create_cube(self, topleft, static = False, rnd = [3, 5]):
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
                self.create_dot(topleft, static, ltr, pg.Vector2(random.randint(rnd[0], rnd[1]), random.randint(rnd[0], rnd[1])))

        connections = ['AB', 'AC', 'CD', 'BD', 'AE', 'BF', 'CG', 'DH', 'EG', 'GH', 'HF', 'FE']

        spr = self.spr

        self.connecting_conf = [f'{ltr1}{ltr2}' for ltr1 in ltrs for ltr2 in ltrs]
        self.vectors = [[body.vector.x, body.vector.y] for body in spr]

        return self.vectors, self.connecting_conf

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
                expconnected_a = list(filter(lambda x: x.letter == a, self.spr))
                expconnected_b = list(filter(lambda x: x.letter == b, self.spr))
                for dot in expconnected_a:
                    for i in expconnected_b:
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

    def run(self, *args):
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
            try:
                self.trail_lines()
            except Exception:
                raise Exception('Не указан параметр соединения точек -> game.trail_conf; для примера: ["A", "B", "C"]')

            for arg in args:
                try: arg()
                except Exception: pass

            self.clock.tick(self.fps)
