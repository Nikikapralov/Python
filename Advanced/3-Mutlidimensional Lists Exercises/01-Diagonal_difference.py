size_of_square_matrix = int(input())
matrix = []
for _ in range(size_of_square_matrix):
    matrix.append([int(x) for x in input().split()])


def find_primary(matrix, size):
    sum_prim = 0
    for row in range(size):
        sum_prim += matrix[row][row]
    return sum_prim


def find_secondary(matrix, size):
    sum_second = 0
    for row in range(size):
        sum_second += matrix[row][size - 1 - row]
    return sum_second


primary = find_primary(matrix, size_of_square_matrix)
secondary = find_secondary(matrix, size_of_square_matrix)
result = abs((primary - secondary))
print(result)
