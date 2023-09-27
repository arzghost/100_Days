from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
from size_of_screen import WIDTH, HEIGHT
import time
from food import Food


version = '0.2'

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title(f'Snake {version}')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.textinput('I\'m waiting for your text', 'Press any key: ')

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision with food
    if snake.head.distance(food) <= 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    #Collision with wall
    if snake.head.xcor() > WIDTH // 2 or snake.head.xcor() < - WIDTH // 2 \
    or snake.head.ycor() > HEIGHT // 2 or snake.head.ycor() < - HEIGHT // 2:
        game_is_on = False
        scoreboard.write_record()
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.write_record()
            scoreboard.game_over()

screen.exitonclick()
