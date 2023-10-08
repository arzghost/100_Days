from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.goto(-300, 260)
        self.level = 1

    def level_increaser(self):
        self.level += 1
    
    def writer(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)