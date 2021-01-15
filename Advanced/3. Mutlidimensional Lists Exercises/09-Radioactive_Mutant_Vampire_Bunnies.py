rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([x for x in input()])
commands = [x for x in input()]


def get_player_position(matrix, rows, cols):
    position = []
    for row in range(rows):
        for col in range(cols):
            potential_position = matrix[row][col]
            if potential_position == 'P':
                position = [row, col]
    return position


def get_bunny_positions(matrix, rows, cols):
    positions = []
    for row in range(rows):
        for col in range(cols):
            potential_position = matrix[row][col]
            if potential_position == 'B':
                positions.append([row, col])
    return positions


def spread_bunnies(matrix, rows, cols, current_bunny_positions):
    bunny_gets_you = False
    for bunny in current_bunny_positions:
        b_row = bunny[0]
        b_col = bunny[1]
        if 0 <= b_row - 1 < rows and 0 <= b_col < cols:  #UP
            if matrix[b_row - 1][b_col] == 'P':
                bunny_gets_you = True
            matrix[b_row - 1][b_col] = 'B'
        if 0 <= b_row + 1 < rows and 0 <= b_col < cols:  #DOWN
            if matrix[b_row + 1][b_col] == 'P':
                bunny_gets_you = True
            matrix[b_row + 1][b_col] = 'B'
        if 0 <= b_row < rows and 0 <= b_col - 1 < cols:  #LEFT
            if matrix[b_row][b_col - 1] == 'P':
                bunny_gets_you = True
            matrix[b_row][b_col - 1] = 'B'
        if 0 <= b_row < rows and 0 <= b_col + 1 < cols: #RIGHT
            if matrix[b_row][b_col + 1] == 'P':
                bunny_gets_you = True
            matrix[b_row][b_col + 1] = 'B'

    return bunny_gets_you, matrix


current_position = get_player_position(matrix, rows, cols)
for command in commands:
    c_row = current_position[0]
    c_col = current_position[1]
    stumbled_upon_bunny = False
    escaped = False
    if command == 'U':
        if 0 <= c_row - 1 < rows and 0 <= c_col < cols:
            if matrix[c_row - 1][c_col] == 'B':
                stumbled_upon_bunny = True
                current_position = [c_row - 1, c_col]
            else:
                current_position = [c_row - 1, c_col]
        else:
            escaped = True
            matrix[current_position[0]][current_position[1]] = '.'
    elif command == 'D':
        if 0 <= c_row + 1 < rows and 0 <= c_col < cols:
            if matrix[c_row + 1][c_col] == 'B':
                stumbled_upon_bunny = True
                current_position = [c_row + 1, c_col]
            else:
                current_position = [c_row + 1, c_col]
        else:
            escaped = True
            matrix[current_position[0]][current_position[1]] = '.'

    elif command == 'L':
        if 0 <= c_row < rows and 0 <= c_col - 1 < cols:
            if matrix[c_row][c_col - 1] == 'B':
                stumbled_upon_bunny = True
                current_position = [c_row, c_col - 1]
            else:
                current_position = [c_row, c_col - 1]
        else:
            escaped = True
            matrix[current_position[0]][current_position[1]] = '.'

    elif command == 'R':
        if 0 <= c_row < rows and 0 <= c_col + 1 < cols:
            if matrix[c_row][c_col + 1] == 'B':
                stumbled_upon_bunny = True
                current_position = [c_row, c_col + 1]
            else:
                current_position = [c_row, c_col + 1]
        else:
            escaped = True
    if not stumbled_upon_bunny:
        matrix[current_position[0]][current_position[1]] = 'P'
        matrix[c_row][c_col] = '.'

    current_bunny_positions = get_bunny_positions(matrix, rows, cols)
    bunny_gets_you, matrix = spread_bunnies(matrix, rows, cols, current_bunny_positions)
    if bunny_gets_you or stumbled_upon_bunny or escaped:
        break
[print("".join([str(x) for x in line])) for line in matrix]
if bunny_gets_you or stumbled_upon_bunny:
    print(f'dead: {current_position[0]} {current_position[1]}')
if escaped:
    print(f'won: {current_position[0]} {current_position[1]}')
#1 2
#PB
#R