import sys
rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
size = 3
current_square = []
biggest = -sys.maxsize


def find_square(matrix, size, start_row, start_col):
    potential_square = []
    summed = 0
    for row in range(start_row, start_row + size):
        pair = []
        for col in range(start_col, start_col + size):
            summed += matrix[row][col]
            pair.append(matrix[row][col])
        potential_square.append(pair)
    return potential_square, summed


for row in range(rows - size + 1):
    for col in range(cols - size + 1):
        potential, current_biggest = find_square(matrix, size, row, col)
        if current_biggest > biggest:
            current_square = [x for x in potential]
            biggest = current_biggest

print(f'Sum = {biggest}')
for pair in current_square:
    pair = [str(item) for item in pair]
    print(' '.join(pair))


