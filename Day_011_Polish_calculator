import operator
import math


OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '^': operator.pow
}

def calculator(array: list) -> float:
    values = []
    for elem in array:
        if all([(i.isdigit() or i == '.') and i.count('.') <= 1 for i in elem]):
            values.append(float(elem))
        elif elem in OPS:
            try:
                b = values.pop()
                a = values.pop()
                values.append(OPS[elem](a, b))
            except IndexError as e:
                print(f'You wrote incorrect expression: {e}')
        else:
            print(f'Unknown operation: {elem}')
    return values[-1] if values[-1] != math.trunc(values[-1]) else math.trunc(values[-1])



def main() -> int:
    # array = input('Enter your expression in Polish reversed notation:\n').split()
    array = '7 8 - 6.5 + 0.5 + 2 ^ 5 % 10 * 3 //'.split()
    print(calculator(array))
    return 0


if __name__ == '__main__':
    main()