size_of_square_matrix = int(input())
matrix = []
for _ in range(size_of_square_matrix):
    matrix.append([int(x) for x in input().split()])
diagonal_sum = 0
for row in range(size_of_square_matrix):
    for column in range(size_of_square_matrix):
        if row == column:
            diagonal_sum += matrix[row][column]
print(diagonal_sum)



