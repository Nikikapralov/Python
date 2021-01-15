numbers = [int(x) for x in input().split(', ')]
positive = {'Positive': [int(x) for x in numbers if x >= 0]}
negative = {'Negative': [int(x) for x in numbers if x < 0]}
even = {'Even': [int(x) for x in numbers if x % 2 == 0]}
odd = {'Odd': [int(x) for x in numbers if x % 2 == 1]}
[print(f'{key}: {", ".join([str(x) for x in value])}') for dictionary in [positive, negative, even, odd] for key, value in dictionary.items()]