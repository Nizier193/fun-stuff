import pygame as pg

objects = pg.sprite.Group()
blocks = pg.sprite.Group()
class Game():
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((500, 500))
        pg.display.set_caption('bouncy')

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()


            self.screen.fill((200, 200, 200))
            objects.update()
            objects.draw(self.screen)

            blocks.update()
            blocks.draw(self.screen)
            pg.display.update()

class Block(pg.sprite.Sprite):
    def __init__(self, size, pos):
        super(Block, self).__init__()
        self.add(blocks)

        self.image = pg.Surface(size=size)
        self.rect = self.image.get_rect(topleft = pos)

class Body(pg.sprite.Sprite):
    gravity_constant = 1
    delta_time = 1

    def __init__(self, size, pos):
        super(Body, self).__init__()
        self.add(objects)

        self.image = pg.Surface(size=size)
        self.rect = self.image.get_rect(topleft = pos)

    def gravity(self):
        self.velocity = pg.Vector2(0, 2)

        self.coll()

        self.velocity.y += self.gravity_constant * self.delta_time
        self.rect.y += self.velocity.y

    def coll(self):
        if pg.sprite.spritecollide(self, blocks, False):
            self.velocity.y *= -1

    def update(self):

        self.gravity()
        print(self.velocity)

Block((500, 20), (0, 500))
Body((5, 5), (150, 0))

game = Game()
game.run()