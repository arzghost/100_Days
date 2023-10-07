from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Comic Sans', 36, 'normal')

class Victory(Turtle):
    def __init__(self, player_position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.player_position = player_position
        self.color('white')
        
    def writer(self):
        self.write(f'{self.player_position} player wins!', align=ALIGNMENT, font=FONT)