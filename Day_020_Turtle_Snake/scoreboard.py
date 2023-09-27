from turtle import Turtle
from size_of_screen import WIDTH, HEIGHT

ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')
FONT_GAME_OVER = ('Courier', 48, 'normal')
COLOR = 'white'

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.score = 0
        self.color(COLOR)
        self.goto(0, HEIGHT // 2 - 40)
        self.read_record()
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}     Record: {self.record}', align=ALIGNMENT, font=FONT)

    def read_record(self):
        try: 
            file = open('record.txt', 'r')
        except FileNotFoundError:
            self.record = 0
        else:
            value = file.readline()
            try:
                self.record = int(value)
            except ValueError:
                self.record = 0
            file.close()

    def write_record(self):
        file = open('record.txt', 'w')
        if self.score > int(self.record):
            file.write(str(self.score))
            file.close()    

    def game_over(self):
        self.color(COLOR)
        self.goto(0, 0)
        self.write('Game over', align=ALIGNMENT, font=FONT_GAME_OVER)
        self.hideturtle