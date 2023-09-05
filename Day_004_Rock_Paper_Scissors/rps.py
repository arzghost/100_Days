import random
import time
import os
import sys


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

RPS = (rock, paper, scissors)
user_points, computer_points, draws_points = 0, 0, 0


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def print_combinations(left, right, word=None):
    left = left.split('\n')
    right = [line[::-1] for line in right.replace(')', '!').replace('(', ')').replace('!', '(').split('\n')]

    for i in range(len(left)):
        print(left[i] + ' ' * (40 - len(left[i]) - len(right[i])) + right[i])
    if word:
        print(f'                  {word}')

def show(left, right, word=None):
    print_combinations(left, right, word)
    time.sleep(1)
    cls()


while True:
    answer = -1
    while answer == -1:
        print('It\'s a Rock-Paper-Scissors game.')
        try:
            answer = int(input('Make your choice:\n0 - Rock\n1 - Paper\n2 - Scissors\n'))
        except ValueError:
            print('Incorrect symbol')
            time.sleep(1)
            cls()
            answer = -1
        else:
            if answer not in tuple(range(0, 3)):
                print('You symbol must be 0, 1 or 2')
                time.sleep(1)
                cls()
                answer = -1
            else:
                cls()
            
            
    computer = random.randint(0, 2)
    for idx, elem in enumerate(RPS):
        print('You' + ' ' * 29 + 'Computer')
        show(elem, elem, ('Rock', 'Paper', 'Scissors')[idx])


    print_combinations(RPS[answer], RPS[computer])
    result = ['draw', 'human', 'computer'][answer - computer]
    if result == 'draw':
        print('It\'s a draw!')
        draws_points += 1
    elif result == 'human':
        print('You win, congratulations!')
        user_points += 1
    else:
        print('You lose.')
        computer_points += 1
    
    print(f'User wins: {user_points}        Computer points: {computer_points}')
    print(f'                Draws: {draws_points}')

    try_again = input('Press any key and then enter if you want to play try again or only enter to exit: ')
    if not try_again:
        print('Goodbye!')
        time.sleep(0.5)
        sys.exit()
    else:
        cls()