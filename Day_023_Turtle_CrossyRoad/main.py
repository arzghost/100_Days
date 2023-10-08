import time
from turtle import Screen, Turtle
from player import Player
from car import CarLine
from lose import End
from scoreboard import Scoreboard


VERSION = '0.1'
Y_CORS = [i for i in range(-240, 241, 60)]
SLEEPER = 0.1


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title(f'Crossy road {VERSION}')

player = Player()
cars = []
for y in Y_CORS:
    cars.append(CarLine(y))
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.down, 'Down')
screen.onkeypress(player.up, 'Up')
screen.onkeypress(player.left, 'Left')
screen.onkeypress(player.right, 'Right')

end = End()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SLEEPER / (2 ** (scoreboard.level - 1)))
    scoreboard.writer()
    
    if player.ycor() > 280:
        player.vin()
        scoreboard.level_increaser()
    
    for line in cars:
        for car in line.cars:
            car.move_car()

    #Colision with cars
    for line in cars:
        if abs(line.y_pos - player.ycor()) <= 10:
            for car in line.cars:
                if abs(player.xcor() - car.xcor()) < 15:
                    end.lose()
                    game_is_on = False
    
    if scoreboard.level == 6:
        end.win()

screen.exitonclick()
