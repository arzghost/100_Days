from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color('#FFFFFF')
        self.setposition(x_cor, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y <= 260:
            self.goto(self.xcor(), new_y)
    
    def move_down(self):
        new_y = self.ycor() - 20
        if new_y >= -240:
            self.goto(self.xcor(), new_y)
