import json
import os


path = os.path.dirname(__file__)

try:
    with open(os.path.join(path, 'books.json'), 'r') as inf:
        books = json.load(inf)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    books = []


while True:
    while True:
        try:
            command = int(input('''Enter what would you like to do:\n1 - add data:\n2 - print data\n3 - delete book\n'''))
        except ValueError:
            print("Incorrect value")
        else:
            if command in tuple(range(1, 4)):
                break
            else:
                print('You wrote the wrong number, there is no such command')
    if command == 1:
        books.append({'title': input('Write the title: '), 'author': input('Write the author: '), 'description': input('Write some description or just press Enter: ')})
    elif command == 2:
        for dct in books:
            for key, value in dct.items():
                print(f'{key.title()}: {value}')
            print('\n')
    else:
        title = input('Enter the title of book which you want to delete: ')
        indices = []
        for idx, dct in enumerate(books):
            if dct['title'].lower() == title.lower():
                indices.append(idx)

        if len(indices) == 0:
            print('There is no book with such title.')
        else:
            for idx in indices[::-1]:
                dct = books.pop(idx)
                print(f"{dct['title']} by {dct['author']} is deleted.")

    enter = input('Enter any key and press Enter to continue or only Enter to exit: ')
    if not enter:
        break

try:
    with open(os.path.join(path, 'books.json'), 'w') as ouf:
        json.dump(ouf, books)
except Exception as e:
    print(f'Sorry, something went wrong. Mistake: {e}')
    
 