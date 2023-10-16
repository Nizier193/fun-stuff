import turtle

turtle.bgcolor("black")
turtle.title("Fractal Tree Pattern")
turtle.left(90)
turtle.speed(0)


def draw(l, color, pensize, n1, n2):
    if (l < 10):
        return
    else:
        turtle.pensize(pensize)
        turtle.pencolor(color)
        turtle.forward(l)
        turtle.left(30)
        draw(n1 * l / n2, color, pensize, n1, n2)
        turtle.right(60)
        draw(n1 * l / n2, color, pensize, n1, n2)
        turtle.left(30)
        turtle.pensize(pensize)
        turtle.backward(l)


draw(20, "yellow", 2, 3, 4)
turtle.right(90)

draw(20, "magenta", 2, 3, 4)
turtle.left(270)

draw(20, "red", 2, 3, 4)
turtle.right(90)

draw(20, "#FFF8DC", 2, 3, 4)

draw(40, "lightgreen", 3, 4, 5)
turtle.right(90)

draw(40, "red", 3, 4, 5)
turtle.left(270)

draw(40, "yellow", 3, 4, 5)
turtle.right(90)

draw(40, "#FFF8DC", 3, 4, 5)

draw(60, "cyan", 2, 6, 7)
turtle.right(90)

draw(60, "yellow", 2, 6, 7)
turtle.left(270)

draw(60, "magenta", 2, 6, 7)
turtle.right(90)

draw(60, "#FFF8DC", 2, 6, 7)

turtle.exitonclick()