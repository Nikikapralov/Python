size = int(input())
field = [[0 for x in range(size)] for line in range(size)]
amount_bombs = int(input())


def is_valid_position(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    else:
        return False


for _ in range(amount_bombs):
    current_bomb = input().split('(')
    current_bomb_2 = ''.join(current_bomb).split(')')
    current_bomb_3 = ''.join(current_bomb_2).split(', ')
    row = int(current_bomb_3[0])
    col = int(current_bomb_3[1])

    if is_valid_position(row, col, size):
        field[row][col] = '*'

for row in range(size):
    for col in range(size):
        current_position = field[row][col]
        if current_position == '*':
            continue
        if is_valid_position(row - 1, col, size):
            up = field[row - 1][col]
            if up == '*':
                field[row][col] += 1
        if is_valid_position(row + 1, col, size):
            down = field[row + 1][col]
            if down == '*':
                field[row][col] += 1
        if is_valid_position(row, col - 1, size):
            left = field[row][col - 1]
            if left == '*':
                field[row][col] += 1
        if is_valid_position(row, col + 1, size):
            right = field[row][col + 1]
            if right == '*':
                field[row][col] += 1
        if is_valid_position(row - 1, col + 1, size):
            right_diagonal_up = field[row - 1][col + 1]
            if right_diagonal_up == '*':
                field[row][col] += 1
        if is_valid_position(row - 1, col - 1, size):
            left_diagonal_up = field[row - 1][col - 1]
            if left_diagonal_up == '*':
                field[row][col] += 1
        if is_valid_position(row + 1, col + 1, size):
            right_diagonal_down = field[row + 1][col + 1]
            if right_diagonal_down == '*':
                field[row][col] += 1
        if is_valid_position(row + 1, col - 1, size):
            left_diagonal_down = field[row + 1][col - 1]
            if left_diagonal_down == '*':
                field[row][col] += 1

[print(' '.join([str(item) for item in x])) for x in field]


