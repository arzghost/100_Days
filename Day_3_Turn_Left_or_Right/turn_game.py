import random
import sys
import time


LEFT_RIGHT = ('left', 'right')
LEFT_CENTER_RIGHT = ('left', 'center', 'right')
TROLLEY_LADDER = ('trolley', 'ladder')
CHEST = r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`'''

c = 0

while True:
    if c == 0:
        print("""You are entring into the deep dark cave to find the treasure.
Your exit was blocked by suddenly fallen stone. 
Now you see two corridors. Will you choose to turn left or right?""")
        c += 1
    answer = input("Type your answer: ").strip().lower()
    if answer in LEFT_RIGHT:
        correct = random.choice(LEFT_RIGHT)
        if answer == correct:
            print(f'It was good choice to turn {correct}.')
            c = 0
            break
        else:
            print('And you meet the giant bear here. He will have a tasty lunch. Game over.')
            input('Press enter to exit.')
            sys.exit()

while True:
    if c == 0:
        time.sleep(2)
        print("""\n\nAfter 15 minutes you enter the room with three doors.
They are absolutely similar, so you may need to throw a coin three times to choose.""")
        c += 1
    answer = input('Where will you go: left, center or right? Type your answer: ').strip().lower()
    if answer in LEFT_CENTER_RIGHT:
        correct = random.choice(LEFT_CENTER_RIGHT)
        if answer == correct:
            c = 0
            print(f'Great! The {correct} door was a great choice!')
            break
        else:
            print(f'''The door suddenly closes when you ctep into the dark room. 
You hear a quiet hissing and feel you're bitten.
Viper rapidly spreads into your body. The {answer} door was a bad choice. Game over!''')
            input('Press enter to exit.')
            sys.exit()


while True:
    if c == 0:
        time.sleep(2)
        print("""\n\nYou finally found a treasure. But how will you get out?
You see the trolley on the rails and the ladder. What will you choose?""")
        c += 1
    answer = input('Make your choice - trolley or ladder? Type your answer: ').strip().lower()
    if answer in TROLLEY_LADDER:
        correct = random.choice(TROLLEY_LADDER)
        if answer == correct:
            print(f'''You successfully ran out with your treasure. Congratulation!
                  {CHEST}''')
        else:
            print(f'''You were too grid, so you took too much and broke your spine. Game over!''')
        input('Press enter to exit.')
        sys.exit()