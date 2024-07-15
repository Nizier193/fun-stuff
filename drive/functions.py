def grid(px, width, height, game, col = (30, 30, 30), showaxis = True):
    # horizontal axis
    for i in range(width // px):
        y_axis = i * px
        game.create_line((0, y_axis), (width, y_axis), (30, 30, 30))

    for y in range(height // px):
        x_axis = y * px
        game.create_line((x_axis, 0), (x_axis, height), (30, 30, 30))

    if showaxis:
        for ax in game.spr:
            coordinates = ax.rect.topleft
            game.create_line((0, coordinates[1]), (width, coordinates[1]), (50, 50, 50))
            game.create_line((coordinates[0], 0), (coordinates[0], height), (50, 50, 50))

def ray_trace(mouse_pos, topleft, ray_tracer, game, col = (50, 50, 50), n_bounce = 0):
    '''

    Строит траекторию полета снаряда.
    Угол падения равен углу отражения.

    Заданное количество отражений.

    '''

    try:
        diff_x = topleft[0] - mouse_pos[0]
        diff_y = topleft[1] - mouse_pos[1]

        cf = diff_y / diff_x
    except Exception:
        diff_x = mouse_pos[0] - topleft[0]
        diff_y = topleft[1] - mouse_pos[1]

        cf = 1e10

    sign_x = -1 if diff_x < 0 else 1
    sign_y = -1 if diff_y < 0 else 1

    p = ray_tracer.calc(cf, topleft[0], topleft[1], sign=(sign_x, sign_y))
    game.create_line(topleft, (p[0], p[1]), col)

    c = -1
    for i in range(n_bounce):
        p2 = ray_tracer.calc(cf * c, p[0], p[1], sign=(-p[2][0], p[2][1]))
        game.create_line((p[0], p[1]), (p2[0], p2[1]), col)

        c *= -1
        p = p2

    return p, cf, topleft