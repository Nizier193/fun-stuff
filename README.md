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

# Последние обновления и модули
Проект неслабо развился, если учитывать то, что это были отскакивающие квадратики. Теперь есть система трасировки лучей.
Ну.. Не совсем трасировки лучей конечно, но небольшие предпосылки к её созданию. Есть рабочая система расчёта координат - 
модуль Ray_Tracer.

Ниже приведён образец с маленьким интерфейсом и красивой анимацией рикошета.

```python
import numpy as np
from random import randint as rand
from functions import *

borders = (1000, 1000)
game = Game(borders, borders=True, fps=60)
font = pg.font.SysFont('Arial', 25)

# Количество отскоков от стен.
n_bounce = 3

# Объекты.
example_dot = game.create_dot((300, 300), vector=(rand(-5, 5), rand(-5, 5)))

# Вспомогательный модуль подсчёта.
ray_tracer = Ray_Tracer(1000, 1000)

def show_m():
    # Рандомная функция для работы.
    # В целом можно написать абсолютно что угодно.

    mouse_pos = pg.mouse.get_pos()

    s = 0
    for sprite in game.spr:
        topleft = sprite.rect.center
        
        # Вспомогательная функция создания "трасировки лучей"
        info = ray_trace(mouse_pos, topleft, n_bounce, ray_tracer, game)

        # На половине отрезка от мыши до объекта пишется любая информация ;; dst.
        dst = round(np.sqrt(np.power(topleft[0] - mouse_pos[0], 2) + np.power(topleft[1] - mouse_pos[1], 2)), 6)
        
        text = font.render(f'{dst}', False, (200, 200, 200))
        game.screen.blit(text, abs(np.array(topleft) + np.array(mouse_pos)) / 2)

        s += dst

    text = font.render(f'{round(s)}', False, (255, 255, 255))
    game.screen.blit(text, (20, 20))

    text = font.render(f'Euclidian dist.', False, (255, 255, 255))
    game.screen.blit(text, (20, 50))

def custom():
    # Эта функция вызывается непосредственно в модуле run корневой системы.
    # Она передаётся в функцию, где происходит обновление фреймов.
    
    grid(50, 1000, 1000, game, showaxis=True)
    show_m()

game.custom = lambda: custom()

game.run()

```

Знаю, прога в целом ничего интересного из себя не представляет, но выглядит забавно и есть
перспективы для развития.

Добавлен пакет с функциями functions. Там их две - ray_trace и grid.
Почитать можно в самой проге.