import turtle
import random


COLORS = [[random.randint(0, 255) for _ in range(3)] for _ in range(6)]
length = 0
STEP = 30

screen = turtle.Screen()
miles = turtle.Turtle()
miles.shape('turtle')
screen.bgcolor("black")
miles.left(165)
miles.speed(100)
turtle.colormode(255)

def square(side):
  for _ in range(4):
    miles.forward(side)
    miles.right(90)
    
for i in range(6):
    miles.right(5)
    length += STEP
    miles.pencolor(COLORS[i])
    for _ in range(12):
        square(length)
        miles.right(30)

miles.hideturtle()

screen.exitonclick()
