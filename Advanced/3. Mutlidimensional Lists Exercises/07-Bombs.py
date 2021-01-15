size = int(input())
matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])
bomb_coordinates = [[int(x) for x in pair.split(',')] for pair in input().split()]


def explode(bomb):
    p_rows = [-1, -1, -1, 0, 0, 1, 1, 1]
    p_cols = [0, 1, -1, -1, 1, 0, 1, -1]
    row_b = bomb[0]
    col_b = bomb[1]
    bomb_value = matrix[row_b][col_b]
    if bomb_value > 0:
        for i in range(len(p_rows)):
            row = row_b + p_rows[i]
            col = col_b + p_cols[i]
            if 0 <= row < len(matrix) and 0 <= col < len(matrix):
                if matrix[row][col] > 0:
                    matrix[row][col] -= bomb_value
        matrix[row_b][col_b] = 0
    else:
        return


for bomb in bomb_coordinates:
    explode(bomb)

alive_cells = 0
sum_of_alive = 0
for row in range(len(matrix)):
    for col in range(len(matrix)):
        cell = matrix[row][col]
        if cell > 0:
            sum_of_alive += cell
            alive_cells += 1

print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_of_alive}')
matrix = [print(" ".join([str(x) for x in line])) for line in matrix]


