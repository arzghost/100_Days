from turtle import Turtle
from random import choice, randint

VELOCITY = 0.05


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = choice([-10, 10])
        self.y_move = choice([-10, 10])
        self.velocity = VELOCITY
    
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.velocity *= 0.5

    def out_of_screen(self):
        self.goto(0, randint(-100, 100))
        self.velocity = VELOCITY
        self.bounce_x()