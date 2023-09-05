import random, os
clear = lambda: os.system('cls')
logo = '''
 _       _____  ____    _   ___      ___       ___  _____  ____    _ 
| |     |  _  ||    \  | | /        |   \     /   ||  _  ||    \  | |
| |____ | |_| || | \ \ | | |    ___ | |\ \   / /| || |_| || | \ \ | |
|  __  ||  _  || |  \ \| | |      | | | \ \_/ / | ||  _  || |  \ \| |
|_|  |_||_| |_||_|   \___| \______/ |_|  \___/  |_||_| |_||_|   \___|
'''

hangman_pics = [
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

possible_words = {"physics": ["электричество", "магнетизм", "электромагнетизм",
"интерференция", "дифракция", "перемещение", "поляризация", "полупроводник"],
"mathematics": ["вектор", "асимптота", "функция", "конъюнкция", "дизъюнкция",
"индукция", "прогрессия", "дифференциал", "интегрирование", "линеаризация"]}


def reduce(lst):
      result = list()
      for i in lst:
            result += i
      return result


if __name__ == "__main__":
      word = list(random.choice(reduce(list(possible_words.values()))))
      answer = list('_' * len(word))
      incorrect_counter = 0
      entered_letters = ''
      flag_win = False
      while incorrect_counter < len(hangman_pics) - 1 and not flag_win:
            print(logo)
            print('Ваше слово: ')
            print(''.join(answer), end='\n')
            print(hangman_pics[incorrect_counter], end = '\n')
            letter = input('Введите одну букву: ').lower()
            if len(letter) > 1 or letter not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                  print('У Вас не получилось, попробуйте ещё раз.')
            else:
                  if letter not in word:
                        if letter in entered_letters:
                              print('Такая буква уже использовалась.')
                        else:
                              incorrect_counter += 1
                              entered_letters += letter
                              print('Такой буквы нет.\n\n')
                  else:
                        for i in range(len(word)):
                              if word[i] == letter:
                                    answer[i] = letter
                              entered_letters += letter
                        if '_' not in answer:
                              print('Вы победили!')
                              flag_win = True
            clear()
      if not flag_win:
            print(hangman_pics[-1])
            print('Вы проиграли...')
      word = ''.join(word)
      print(f'Загаданное слово: {word}')