N1 = int(input())
N2 = int(input())
operator = input()
result = 0
is_even_or_odd = result % 2 == 0

if operator == '+':
    result = N1 + N2
    is_even_or_odd = result % 2 == 0
    if is_even_or_odd:
        print(f'{N1} {operator} {N2} = {result} - even')
    elif is_even_or_odd == False:
        print(f'{N1} {operator} {N2} = {result} - odd')
elif operator == '-':
    result = N1 - N2
    is_even_or_odd = result % 2 == 0
    if is_even_or_odd:
        print(f'{N1} {operator} {N2} = {result} - even')
    elif is_even_or_odd == False:
        print(f'{N1} {operator} {N2} = {result} - odd')
elif operator == '*':
    result = N1 * N2
    is_even_or_odd = result % 2 == 0
    if is_even_or_odd:
        print(f'{N1} {operator} {N2} = {result} - even')
    elif is_even_or_odd == False:
        print(f'{N1} {operator} {N2} = {result} - odd')
if (N2 == 0) and (operator == '/' or operator == '%'):
    print(f'Cannot divide {N1} by zero')

elif operator == '/':
        result = N1 / N2
        print(f'{N1} {operator} {N2} = {result:.2f}')
elif operator == '%':
    result = N1 % N2
    print(f'{N1} % {N2} = {result}')