from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('green')
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
    
    def left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
    
    def vin(self):
        self.goto(STARTING_POSITION)