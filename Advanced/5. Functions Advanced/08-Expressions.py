from itertools import chain
from itertools import product

initial_list = [x for x in input().split(', ')]

result = product('+-', repeat=len(initial_list))

for permutation in result:
    zipped = zip(permutation, initial_list)
    expression = ''.join(list(chain(*zipped)))
    result = eval(expression)
    print(f'{expression}={result}')
