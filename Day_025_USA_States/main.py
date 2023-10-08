import turtle as tr
import pandas as pd
from written_name import Name

IMAGE = r'blank_states_img.gif'
DATA =  r'states.csv'
data = pd.read_csv(DATA)
statenames = data.state.to_list()


screen = tr.Screen()
screen.tracer(0)
screen.addshape(IMAGE)
tr.shape(IMAGE)
screen.setup(width=730, height=500)


correct_answers = 0

game_is_on = True
while game_is_on:
    title = screen.textinput(title=f'({correct_answers}/50) states correct', prompt='Enter state name: ')
    if title == None:
        game_is_on = False
        with open(r'states_to learn.csv', 'w') as ouf:
            for stname in statenames:
                ouf.write(f'{stname}\n')
    else:
        title = title.strip().title()
        if title in statenames:
            index = statenames.index(title)
            del statenames[index]
            x, y = int(data[data.state == title].x), int(data[data.state == title].y)
            name = Name(x, y, title)
            correct_answers += 1
        if correct_answers == 50:
            game_is_on = False
            tim = tr.Turtle()
            tim.hideturtle()
            tim.write('Victory!', align='center', font=('Comic Sans', '24', 'normal'))

screen.exitonclick()
