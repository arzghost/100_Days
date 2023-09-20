from turtle import Turtle, Screen
from math import sin, pi


screen = Screen()

def draw_nfigure(miles: Turtle, n: int, length: int) -> None:
    miles.hideturtle()
    miles.left(90)
    miles.up()
    miles.forward(length / (2 * sin(pi / n)))
    miles.right(90)
    miles.backward(length / 2)
    miles.down()
    miles.fillcolor('red')
    miles.showturtle()
    miles.begin_fill()
    

    for _ in range(n):
        miles.forward(length)
        
        miles.right(360 / n)

    miles.end_fill()
    miles.up()
    miles.hideturtle()
    miles.home()
    miles.down()
    screen.exitonclick()

draw_nfigure(Turtle(shape='turtle'), 6, 150)