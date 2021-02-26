text = input()
try:
    repeats = int(input())
except ValueError:
    print(f'Variable times must be an integer')
    raise ValueError
print(text * repeats)