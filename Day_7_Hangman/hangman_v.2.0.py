import random
import math
import requests
import time
import os
from string import ascii_lowercase as alower


TITLE = """
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝"""

TROPHY = '''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
          '''

HANGMAN_PICS = [
'''
  ----+
      |
      |
      |
______|
''',
'''
 o----+
      |
      |
      |
______|
''',
'''
 o----+
/|\   |
      |
      |
______|
''',
'''
 o----+
/|\   |
 |    |
      |
______|
''',
'''
 o----+
/|\   |
 |    |
/ \   |
______|
'''
]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


is_going = True
while is_going:
    length = math.ceil(random.normalvariate(8, 2))
    secret_word = eval(requests.get(f'https://random-word-api.herokuapp.com/word?length={length}').text)[0].lower()
    c = 0
    already_used = set()
    current_text = ['_' for _ in range(len(secret_word))]
    while '_' in current_text and c < len(HANGMAN_PICS):
        cls()
        print(TITLE)
        print(HANGMAN_PICS[c])
        print(f"Word: {''.join(current_text)}")
        print(f"Already_used: {' '.join(already_used)}")
        symbol = input('Enter one letter: ').lower()
        if len(symbol) == 1 and symbol in alower:
            if symbol in already_used:
                print(f'"{symbol}" has already been used.')
                time.sleep(1)
            else:
                already_used.add(symbol)
                is_changed = False
                if symbol in secret_word:
                    for idx, letter in enumerate(secret_word):
                        if symbol == letter:
                            current_text[idx] = symbol
                            is_changed = True
                if not is_changed:
                    c += 1
        else:
            print(f'Your entered symbol {symbol} does not match requirements.')
            time.sleep(1)
    if ''.join(current_text) == secret_word:
        print('Congratulations, you won!')
        print(TROPHY)
    else:
        print('You lost.')
    print(f'The secret word was: {secret_word}.')
    is_going = '' == input('If you want to play again, press Enter, else press any key and then Enter: ')
