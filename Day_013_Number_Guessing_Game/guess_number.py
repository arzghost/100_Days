import random
from math import log2, ceil


LOW, HIGH = 1, 1000
TOTAL_ATTEMPS = ceil(log2(HIGH - LOW))


class OutOfRange(Exception):
    min_value = LOW
    max_value = HIGH

    def __init__(self, value, *args):
        super().__init__(args)
        self.value = value

    def __str__(self):
        return f'Your value={self.value} if out of range {self.min_value} and {self.max_value}'
    

def is_in_range(value):
    if not LOW <= value <= HIGH:
        raise OutOfRange(value)
    return True


def main():
    while True:
        curr = 0
        number = random.randint(LOW, HIGH)
        attempt = -1
        while attempt != number and curr < TOTAL_ATTEMPS:
            try:
                attempt = int(input('Enter your guessed number: '))
            except ValueError:
                print('You wrote incorrect value.')
            else:
                try:
                    is_in_range(attempt)
                except OutOfRange as ex:
                    print(ex)
                else:
                    if attempt == number:
                        print('You are right. You won!')
                    else:
                        curr += 1
                        print('Your guess is higher.' if attempt > number else 'Your guess is lower.')
                        print(f'Total attempts left: {TOTAL_ATTEMPS - curr}')
        if curr == TOTAL_ATTEMPS:
            print(f'You lost. The number was {number}.')
        not_play_again = input('Press enter to play again or press any key and enter to exit: ')
        if not_play_again:
            break

if __name__ == '__main__':
    main()

        