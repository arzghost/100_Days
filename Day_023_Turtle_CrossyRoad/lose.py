from turtle import Turtle


FONT = ("Courier", 24, "normal")


class End(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def lose(self):
        self.write('You have lost.', align='center', font=FONT)
    
    def win(self):
        self.write('You win! Congratulations!!!', align='center', font=FONT)