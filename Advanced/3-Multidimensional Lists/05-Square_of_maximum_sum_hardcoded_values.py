rows, cols = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(',')]
    matrix.append(row)
current_biggest = [(0,0), (0,0)]
sum_biggest = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > sum_biggest:
            sum_biggest = current_sum
            current_biggest = [(matrix[row][col], matrix[row][col + 1]),
                               (matrix[row + 1][col], matrix[row + 1][col + 1])]

for pair in current_biggest:
    for item in pair:
        print(item, end=' ')
    print()
print(sum_biggest)
