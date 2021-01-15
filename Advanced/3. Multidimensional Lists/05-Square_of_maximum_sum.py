from sys import maxsize
size = int(input())
rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)
current_biggest = [(0, 0) for _ in range(size)]
sum_biggest = -maxsize
such_sum = False

def find_biggest(size, start_col, start_row):
    summed = 0
    potential_biggest = []
    for row in range(start_row, size + start_row):
        pair = []
        for col in range(start_col, size + start_col):
            summed += matrix[row][col]
            pair.append(matrix[row][col])
        potential_biggest.append(pair)

    return summed, potential_biggest

for row in range(rows - size + 1):
    for col in range(cols - size + 1):
        current_sum, potential_biggest = find_biggest(size, col, row)
        if current_sum > sum_biggest:
            sum_biggest = current_sum
            current_biggest = potential_biggest
            such_sum = True
if such_sum:
    for pair in current_biggest:
        for item in pair:
            print(item, end=' ')
        print()
    print(sum_biggest)
else:
    print('No such sum')