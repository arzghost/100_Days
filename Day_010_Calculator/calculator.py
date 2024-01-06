import operator, math

# Доступные операторы
## Поддерживаются только односимвольные
OPS = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
    '/': operator.truediv,
}

def cotan(x):
    return 1 / math.tan(x)

# Доступные функции
FUNCS = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'cotan': lambda x: 1 / math.tan(x),
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan
}


def calc(token):
    try:
        return float(token)

    except ValueError:
        begin = token.find('(')
        if begin == 0 and token[-1] == ')':
            return parse(token[1:-1])

        elif begin > 0 and token[-1] == ')':
            name = token[0:begin]
            if name not in FUNCS:
                raise ValueError('Unknown function %s' % name)
            arg0 = parse(token[begin+1:-1])
            result = FUNCS[name](arg0)
            return result

        else:
            raise ValueError('Unknown token %s' % repr(token))


def parse(txt):
    token = ''
    depth = 0
    op = None
    current_value = None

    def close_token():

        nonlocal token, op, current_value
        if token != '':
            if current_value is None:
                current_value = calc(token)
            else:
                current_value = OPS[op](current_value, calc(token))
                op = None
            token = ''

    for c in txt:
        if depth > 0:
            if c == ' ':
                continue
            token += c
            if c == ')':
                depth -= 1
                close_token()

        elif c == '(':
            if token == '':

                close_token()
            depth += 1
            token += c

        else:
            if c == ' ':
                continue
            elif c in OPS:
                close_token()
                op = c
            else:
                token += c

    close_token()
    return current_value


result = parse(input('Enter your expression: '))
print('Result:', result)
