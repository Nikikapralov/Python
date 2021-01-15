matrix = [[int(x) for x in input().split(', ')] for line in range(int(input()))]
primary_diag = [matrix[row][row] for row in range(len(matrix))]
secondary_diag = [matrix[row][len(matrix) - 1 - row] for row in range(len(matrix))]
diagonals = ['First diagonal', 'Second diagonal']
values = [primary_diag, secondary_diag]
zipped = zip(diagonals, values)
dictionary = {key: value for key, value in zipped}
[print(f'{key}: {", ".join([str(x) for x in value])}. Sum: {sum(value)}') for key, value in dictionary.items()]
