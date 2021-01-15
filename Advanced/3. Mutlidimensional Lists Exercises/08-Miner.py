size = int(input())
directions = input().split()
matrix = []
for _ in range(size):
    matrix.append([x for x in input().split()])
coal_count = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 's':
            current_pos = [row, col]
        elif matrix[row][col] == 'c':
            coal_count += 1
collected_coals = 0
for command in directions:
    c_row = current_pos[0]
    c_col = current_pos[1]
    if command == 'up':
        row_new = c_row - 1
        col_new = c_col
    elif command == 'down':
        row_new = c_row + 1
        col_new = c_col
    elif command == 'right':
        row_new = c_row
        col_new = c_col + 1
    elif command == 'left':
        row_new = c_row
        col_new = c_col - 1
    if 0 <= row_new < size and 0 <= col_new < size:
        current_pos = [row_new, col_new]
        if matrix[row_new][col_new] == 'c':
            matrix[row_new][col_new] = '*'
            coal_count -= 1
            if coal_count == 0:
                print(f'You collected all coals! ({row_new}, {col_new})')
                exit()

        elif matrix[row_new][col_new] == 'e':
            print(f'Game over! ({row_new}, {col_new})')
            exit()
print(f'{coal_count} coals left. ({row_new}, {col_new})')
