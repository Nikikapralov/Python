rows_count, columns_count = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(rows_count):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)
for column in range(columns_count):
    current_column = 0
    for row in matrix:
        current_column += row[column]
    print(current_column)
