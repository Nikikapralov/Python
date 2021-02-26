rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([x for x in input().split()])
command = input()
while command != 'END':
    try:
        swap, row_1, col_1, row_2, col_2 = command.split()
    except ValueError:
        print('Invalid input!')
        command = input()
        continue
    row_1, col_1, row_2, col_2 = int(row_1), int(col_1), int(row_2), int(col_2)
    try:
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
    except IndexError:
        print('Invalid input!')
        command = input()
        continue

    [print(" ".join(x)) for x in matrix]
    command = input()
