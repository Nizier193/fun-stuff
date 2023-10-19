from ricochet import *
import string

game = Game((1000, 1000), trails_lines=True, pre_loaded_asset=False, connect_lines=False, borders=True)

for i, ltr in enumerate(string.ascii_lowercase):
    game.create_dot(pg.Vector2(50, 50), False, ltr, pg.Vector2(i * 2, i))

game.trailed_conf = string.ascii_lowercase
game.run()