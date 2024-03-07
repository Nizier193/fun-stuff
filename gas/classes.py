import pygame as pg
from random import randint as r

map_size = (1000, 1000)
molecules = pg.sprite.Group()


class Molecule(pg.sprite.Sprite):
    def __init__(self):
        super(Molecule, self).__init__()
        self.add(molecules)

        self.velocity = pg.Vector2((r(-5, 5), r(-5, 5)))
        self.image = pg.Surface((5, 5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=(r(0, map_size[1] - 100), r(0, map_size[1] - 100)))

    def coll(self):
        for sprite in pg.sprite.spritecollide(self, molecules, False):
            if sprite != self:
                s_vel = self.velocity
                self_vel = sprite.velocity

                sprite.velocity = s_vel
                self.velocity = self_vel

    def update(self):
        if self.rect.x > map_size[0] or self.rect.x < 0:
            self.velocity.x *= -1
        if self.rect.y > map_size[1] or self.rect.y < 0:
            self.velocity.y *= -1

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.coll()
