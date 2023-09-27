from turtle import Turtle
from size_of_screen import WIDTH, HEIGHT
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('yellow')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-WIDTH // 2 + 20, WIDTH // 2 - 20)
        random_y = random.randint(- HEIGHT // 2 + 20, HEIGHT // 2 - 20)
        self.goto(random_x, random_y)

