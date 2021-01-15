rows_cols_matrix = int(input())
matrix = []
for _ in range(rows_cols_matrix):
    line = [x for x in input()]
    matrix.append(line)
symbol_to_look_for = input()
for row in range(rows_cols_matrix):
    for col in range(rows_cols_matrix):
        if matrix[row][col] == symbol_to_look_for:
            print(f'({row}, {col})')
            exit()
print(f'{symbol_to_look_for} does not occur in the matrix')
