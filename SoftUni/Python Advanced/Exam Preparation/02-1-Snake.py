size = int(input())
matrix = [list(input()) for line in range(size)]


def get_snake_position(matrix, size):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'S':
                position = (row, col)
                return position


def find_other_burrow(b_row, b_col, matrix):
    current_burrow = (b_row, b_col)
    for row in range(size):
        for col in range(size):
            if row == b_row and col == b_col:
                continue
            potential_burrow = matrix[row][col]
            if potential_burrow == 'B':
                return (row, col)


def is_position_valid(matrix, row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


starting_position = get_snake_position(matrix, size)
row = starting_position[0]
col = starting_position[1]
is_out = False
total_food_eaten = 0
eaten_10_food = False
while True:
    command = input()
    if command == 'up':
        if is_position_valid(matrix, row - 1, col):
            if matrix[row - 1][col] == '*':
                total_food_eaten += 1
                matrix[row][col] = '.'
                row = row - 1
                col = col
                matrix[row][col] = 'S'
                if total_food_eaten == 10:
                    eaten_10_food = True
                    break
            elif matrix[row - 1][col] == 'B':
                matrix[row - 1][col] = '.'
                matrix[row][col] = '.'
                other_burrow = find_other_burrow(row - 1, col, matrix)
                row = other_burrow[0]
                col = other_burrow[1]
                matrix[row][col] = 'S'
            else:
                matrix[row][col] = '.'
                row = row - 1
                col = col
                matrix[row][col] = 'S'

        else:
            is_out = True
            matrix[row][col] = '.'
            break
    elif command == 'down':
        if is_position_valid(matrix, row + 1, col):
            if matrix[row + 1][col] == '*':
                total_food_eaten += 1
                matrix[row][col] = '.'
                row = row + 1
                col = col
                matrix[row][col] = 'S'
                if total_food_eaten == 10:
                    eaten_10_food = True
                    break
            elif matrix[row + 1][col] == 'B':
                matrix[row + 1][col] = '.'
                matrix[row][col] = '.'
                other_burrow = find_other_burrow(row + 1, col, matrix)
                row = other_burrow[0]
                col = other_burrow[1]
                matrix[row][col] = 'S'
            else:
                matrix[row][col] = '.'
                row = row + 1
                col = col
                matrix[row][col] = 'S'
        else:
            is_out = True
            matrix[row][col] = '.'
            break
    elif command == 'right':
        if is_position_valid(matrix, row, col + 1):
            if matrix[row][col + 1] == '*':
                total_food_eaten += 1
                matrix[row][col] = '.'
                row = row
                col = col + 1
                matrix[row][col] = 'S'
                if total_food_eaten == 10:
                    eaten_10_food = True
                    break
            elif matrix[row][col + 1] == 'B':
                matrix[row][col + 1] = '.'
                matrix[row][col] = '.'
                other_burrow = find_other_burrow(row, col + 1, matrix)
                row = other_burrow[0]
                col = other_burrow[1]
                matrix[row][col] = 'S'
            else:
                matrix[row][col] = '.'
                row = row
                col = col + 1
                matrix[row][col] = 'S'
        else:
            is_out = True
            matrix[row][col] = '.'
            break
    elif command == 'left':
        if is_position_valid(matrix, row, col - 1):
            if matrix[row][col - 1] == '*':
                total_food_eaten += 1
                matrix[row][col] = '.'
                row = row
                col = col - 1
                matrix[row][col] = 'S'
                if total_food_eaten == 10:
                    eaten_10_food = True
                    break
            elif matrix[row][col - 1] == 'B':
                matrix[row][col - 1] = '.'
                other_burrow = find_other_burrow(row, col - 1, matrix)
                row = other_burrow[0]
                col = other_burrow[1]
                matrix[row][col] = 'S'
            else:
                matrix[row][col] = '.'
                row = row
                col = col - 1
                matrix[row][col] = 'S'
        else:
            is_out = True
            matrix[row][col] = '.'
            break

if is_out:
    print('Game over!')
elif eaten_10_food:
    print('You won! You fed the snake.')
print(f'Food eaten: {total_food_eaten}')
[print(''.join([x for x in line])) for line in matrix]
