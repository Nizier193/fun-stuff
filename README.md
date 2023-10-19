## Симуляция отскакивающих квадратиков

Проект, позволяющий создавать окошко с отскакивающими от препятствий точками.

# Вкратце об использовании
Для создания базового окна с фигурой из 8 вершин, каждая с рандомными значениями скорости от [5, 7] нестатичные; static = False:

``` python
from ricochet import *

game = Game((1000, 1000), trails_lines=False, pre_loaded_asset=False, connect_lines=True, borders=True)

game.create_cube(pg.Vector2(0, 0), False, [5, 7])

game.run()
```

``` python
from ricochet import *

game = Game((1000, 1000), trails_lines=True, pre_loaded_asset=False, connect_lines=False, borders=True)

game.create_dot(pg.Vector2(50, 50), False, 'A', pg.Vector2(10, 20))
game.create_dot(pg.Vector2(50, 50), False, 'B', pg.Vector2(20, 25))
game.create_dot(pg.Vector2(50, 50), False, 'C', pg.Vector2(30, 35))
game.trailed_conf = ['A', 'B', 'C']

game.run()
```

``` python
from ricochet import *
import string

game = Game((1000, 1000), trails_lines=True, pre_loaded_asset=False, connect_lines=False, borders=True)

for i, ltr in enumerate(string.ascii_lowercase):
    game.create_dot(pg.Vector2(50, 50), False, ltr, pg.Vector2(i * 2, i))

game.trailed_conf = string.ascii_lowercase
game.run()
```