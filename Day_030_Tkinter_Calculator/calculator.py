import re
import operator as op

OPS = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '^': op.pow,
    '/': op.truediv,
    '%': op.mod,
}

def is_correct_brackets(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack


def calculate(expression):
    # Определение регулярного выражения для извлечения чисел, операторов и скобок
    pattern = r'(\d+(\.\d*)?|\.\d+|[+\-*/%^()])'
    matches = [match.group(1) for match in re.finditer(pattern, expression)]

    if not is_correct_brackets(expression):
        raise ValueError('Invalid number of brackets.')        

    # Преобразование выражения в обратную польскую запись (постфиксную нотацию)
    output_queue = []
    operator_stack = []

    for token in matches:
        if token.isdigit() or token.replace('.', '').isdigit():
            output_queue.append(token)
        elif token in "+-*/%^":
            while operator_stack and operator_stack[-1] in "+-*/%^" and \
                    (token in "+-" or (token in "*/" and operator_stack[-1] in "*/")):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    # Вычисление результата из обратной польской записи
    stack = []
    for token in output_queue:
        if token.isdigit() or token.replace('.', '').isdigit():
            stack.append(float(token))
        elif token in "+-*/%^":
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(OPS[token](num1, num2))

    return stack[0]

if __name__ == '__main__':
    expression = input("Enter your expression: ")
    result = calculate(expression)
    print(f"Result: {result}")
