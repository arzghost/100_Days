from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from victory import Victory
from time import sleep

VERSION = '0.1'


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title(f'Pong {VERSION}')
screen.tracer(0)

right_paddle = Paddle(380)
left_paddle = Paddle(-380)
ball = Ball()
right_scoreboard = Scoreboard(50)
left_scoreboard = Scoreboard(-50)

screen.listen()

screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')


game_is_on = True
while game_is_on:
    screen.update()
    left_scoreboard.writer()
    right_scoreboard.writer()
    ball.move()
    sleep(ball.velocity)

    #Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with paddles
    if abs(ball.ycor() - right_paddle.ycor()) <= 50  and ball.xcor() == 350 or \
        abs(ball.ycor() - left_paddle.ycor()) <= 50 and ball.xcor() == -350:
        ball.bounce_x()
    elif 350 < ball.xcor() < 400 or -400 < ball.xcor() < -350:
        continue
    elif ball.xcor() > 400:
        left_scoreboard.score_inc()
        left_scoreboard.clear()
        ball.out_of_screen()
    elif ball.xcor() < -400:
        right_scoreboard.score_inc()
        right_scoreboard.clear()
        ball.out_of_screen()
    
    if left_scoreboard.score > 9:
        victory = Victory('Left')
        victory.writer()
        left_scoreboard.writer()
        game_is_on = False
    elif right_scoreboard.score > 9:
        victory = Victory('Right')
        victory.writer()
        right_scoreboard.writer()
        game_is_on = False

screen.exitonclick()