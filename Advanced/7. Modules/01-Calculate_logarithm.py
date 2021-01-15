from math import log
number = int(input())
base = input()
if base == 'natural':
    result = log(number)
else:
    base = int(base)
    result = log(number, base)
print(f'{result:.2f}')