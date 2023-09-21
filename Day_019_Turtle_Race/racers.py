from turtle import Screen, Turtle
import random


screen = Screen()
screen.setup(width = 600, height = 400)
screen.bgcolor('cyan')
colours = ['orange', 'blue', 'purple', 'red']

is_race_on = False
user_bet = ''
while user_bet not in colours:
    user_bet = screen.textinput(title='Make your bet: ', prompt='Enter the color (orange/blue/purple/red): ').strip().lower()

start_position = -180
turtles = [Turtle(shape='turtle', visible=False) for _ in range(4)]

for idx, turtle in enumerate(turtles):
    turtle.color(colours[idx])
    turtle.penup()
    turtle.setposition(-270, start_position)
    start_position += 120
    turtle.showturtle()


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 270:
            winning_color = turtle.color()[1]
            if winning_color == user_bet.lower():
                print(f'You win! The winner is {winning_color} turtle.')
            else:
                print(f'You have lost! The winner is {winning_color} turtle.')
            is_race_on = False
            break


screen.exitonclick()