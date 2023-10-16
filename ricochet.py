import pygame as pg
import math
import random

class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1000, 1000))
        self.clock = pg.time.Clock()

        self.spr = []
        for i in range(8):
            self.spr.append(Dot((random.randint(100, 300), random.randint(100, 300)), '1'))

        self.create_box((-5, -5), 1005, 5)

    def create_box(self, topleft, size, width):
        Block(topleft, (size, width), 'BOTTOM')
        Block(topleft, (width, size), 'SIDES')
        Block((topleft[0], topleft[1] + size), (size, width), 'BOTTOM')
        Block((topleft[0] + size, topleft[1]), (width, size + width), 'SIDES')

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            pg.display.update()
            self.screen.fill((0, 0, 0))

            dots.update(self.screen)
            dots.draw(self.screen)

            for index, dot in enumerate(self.spr):
                for i in self.spr:
                    if i != dot:
                        pg.draw.line(surface=self.screen, color=dot.c,
                                     start_pos=[dot.rect.x, dot.rect.y],
                                     end_pos=[i.rect.x, i.rect.y])

            blocks.update()
            blocks.draw(self.screen)

            self.clock.tick(60)

dots = pg.sprite.Group()
blocks = pg.sprite.Group()
class Dot(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super(Dot, self).__init__()
        self.add(dots)

        self.image = pg.Surface((5, 5))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect(topleft = pos)

        self.group = group
        self.trail = [[self.rect.x, self.rect.y]]
        self.c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

        self.vector = pg.Vector2(
            random.randint(0, 8), random.randint(0, 8)
        )

    def update(self, surface):

        for block in pg.sprite.spritecollide(self, blocks, False):
            if block.type == 'BOTTOM':
                self.trail.append([self.rect.x, self.rect.y])
                self.vector.y *= -1

            if block.type == 'SIDES':
                self.trail.append([self.rect.x, self.rect.y])
                self.vector.x *= -1

        self.rect.x += self.vector.x
        self.rect.y += self.vector.y

class Block(pg.sprite.Sprite):
    def __init__(self, pos, size, type):
        super(Block, self).__init__()
        self.add(blocks)

        self.image = pg.Surface((size[0], size[1]))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect(topleft = pos)

        self.type = type

game = Game()
game.run()
