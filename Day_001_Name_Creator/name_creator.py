from functools import reduce
import random
import os

path = os.path.dirname(__file__)

def choose_from_file(filename):
    with open(os.path.join(path, filename), encoding='utf-8-sig') as inf:
        return random.choice(list(reduce(lambda x, y: x + y, [line.strip().split('\t') for line in inf.readlines()], [])))

animal, action, obj = map(choose_from_file, ('animals.txt', 'actions.txt', 'object.txt'))

print(animal, action, obj)