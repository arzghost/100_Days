from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Comic Sans', 36, 'normal')

class Scoreboard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(x, 250)
        self.score = 0

    def score_inc(self):
        self.score += 1

    def writer(self):
        self.write(f'{self.score}', align= ALIGNMENT, font=FONT)