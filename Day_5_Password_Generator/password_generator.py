import string
import random


consonants = 'bcdfghklmnpqrstvwxz'
vowels = 'aeiouy'
digits = list(string.digits)
puncs = string.punctuation


def up_low(letter: str) -> str:
    return letter if random.randint(0, 1) else letter.upper()

def generate_password() -> string:
    length = random.randint(12, 20)
    result = [random.choice(puncs)]
    number_of_digits = random.randint(4, 8)
    result += random.choices(digits, k=number_of_digits)
    length -= number_of_digits
    result += [up_low(random.choice(seq)) for seq in random.choices([vowels, consonants], weights=[2, 1], k=length - 1)]
    random.shuffle(result)
    return ''.join(result)

print(generate_password())
