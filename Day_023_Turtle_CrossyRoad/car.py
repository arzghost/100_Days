from turtle import Turtle
from random import choice, randint

COLORS = ''.join([str(i) for i in range(0, 10)]) + 'abc'
STEP = 20

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.choose_color()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.direction = 1

    def choose_color(self):
        combination = '#'
        for _ in range(6):
            combination += choice(COLORS)
        self.color(combination)

    def move_car(self):
        self.goto(self.xcor() + STEP * self.direction, self.ycor())
        if self.xcor() >= 310 or self.xcor() <= -310:
            self.goto(-self.xcor(), self.ycor())

class CarLine:
    def __init__(self, y_pos):
        self.cars_number = randint(2, 6)
        self.y_pos = y_pos
        self.x_coords = []
        self.cars = []
        start_x = choice(list(range(-330, -300, 10)) + list(range(310, 340, 10)))
        sign = abs(start_x) // start_x
        possible_x = list(range(start_x, -start_x, -sign * 80))
        
        for _ in range(self.cars_number):
            x = choice(possible_x)
            pos = possible_x.index(x)
            del possible_x[pos]
            self.x_coords.append(x)
    
        self.place_cars()

    def place_cars(self):
        number = choice([-1, 1])
        for i in range(self.cars_number):
            car = Car()
            car.direction = number
            car.goto(self.x_coords[i], self.y_pos)
            self.cars.append(car)
