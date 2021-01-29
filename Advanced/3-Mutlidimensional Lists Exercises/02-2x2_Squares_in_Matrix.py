rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([x for x in input().split()])

identical_squares = 0


def check_square(matrix, col, row):
    is_first = True
    for row_1 in range(row, row + 2):
        for col_1 in range(col, col + 2):
            if is_first:
                symbol = matrix[row_1][col_1]
                is_first = False
                continue
            current_symbol = matrix[row_1][col_1]
            if current_symbol != symbol:
                return False
    return True


for row in range(rows - 1):
    for col in range(cols - 1):
        if check_square(matrix, col, row):
            identical_squares += 1

print(identical_squares)
