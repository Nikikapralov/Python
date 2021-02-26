def solve(string):
    number_1, operator, number_2 = string.split()
    if operator == '^':
        result = float(number_1) ** float(number_2)
        result = f'{result:.2f}'
    else:
        result = f'{eval(string):.2f}'
    #I know it is a security flaw, I just wanted to see if it will work and it kinda does.
    return result
