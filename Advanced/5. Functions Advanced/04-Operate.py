from functools import reduce


def operate(operator, *args):
    if operator == '+':
        return reduce(lambda a, b: a + b, args)
    elif operator == '-':
        return reduce(lambda a, b: a - b, args)
    elif operator == '/':
        return reduce(lambda a, b: a / b if a != 0 and b != 0 else a / b, args)
    elif operator == '*':
        return reduce(lambda a, b: a * b if a != 0 and b != 0 else a * b, args)

print(operate("*", 0, 4))