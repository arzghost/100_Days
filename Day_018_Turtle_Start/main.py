from turtle import Turtle, Screen, colormode
from random import choice


symbols = list(map(str, list(range(10)))) + list('abcdef')


james = Turtle()
james.shape('turtle')
james.color('green')


# Square
# for i in range(4):
#     james.forward(100)
#     james.right(90)


# Dashed line
# james.left(90)
# for i in range(15):
#     james.pendown()
#     james.forward(10)
#     james.penup()
#     james.forward(10)

# Many angles
# def figure(n):
#     color = '#'
#     for i in range(6):
#         color += choice(symbols)
#     james.pencolor(color)
#     for i in range(n):
#         james.forward(100)
#         james.right(180 - 180 * (n - 2) / n)
# 
# for i in range(3, 11):
#     figure(i)


# random walk
steps = 1000
james.pensize(5)
james.speed(500)
while steps > 0:
    color = '#'
    for i in range(6):
        color += choice(symbols)
    james.pencolor(color)
    directions = list(range(0, 271, 90))
    james.right(choice(directions))
    james.forward(10)
    steps -= 1


# # Children circles
# james.speed('fastest')
# n = 100
# colormode(255)
# nums = list(range(0, 256))
# for i in range(n):
#     james.pencolor((choice(nums), choice(nums), choice(nums)))
#     james.circle(100)
#     james.right(360 / n)
# screen = Screen()
# screen.exitonclick()