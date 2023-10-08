from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', '8', 'normal')

class Name(Turtle):
    def __init__(self, x, y, name):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(x, y)
        self.write(name, align=ALIGNMENT, font=FONT)