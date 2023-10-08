with open(r'./Input/Letters/letter_text.txt', 'r') as inf:
    letter_text = inf.read()

with open(r'./Input/Names/invited_names.txt') as inf:
    names = inf.readlines()

for name in names:
    name = name.strip()
    with open(f'./Output/{name}.txt', 'w') as ouf:
        ouf.write(letter_text.replace('[name]', name))