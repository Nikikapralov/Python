'''Challenge: Only 1 "for" cycle for the queens.'''
matrix = [list(input().split()) for line in range(8)]
king_coordinates = [(row, col) for row in range(8) for col in range(8) if matrix[row][col] == 'K']
queen_up = 0
queen_down = 0
queen_left = 0
queen_right = 0
queen_prim_diag_up = 0
queen_prim_diag_down = 0
queen_second_diag_up = 0
queen_second_diag_down = 0
is_queen_up = False
is_queen_left = False
is_queen_prim_diag_up = False
is_queen_prim_diag_down = False
is_queen_second_diag_up = False
is_queen_second_diag_down = False
for i in range(8):
    row = king_coordinates[0][0]
    col = king_coordinates[0][1]
    if matrix[row - i][col] == 'Q':
        if row - i >= 0 and not is_queen_up:
            queen_up = [row - i, col]
            is_queen_up = True
        elif row - i < 0:
            queen_down = [8 + row - i, col]
    if matrix[row][col - i] == 'Q':
        if col - i >= 0 and not is_queen_left:
            queen_left = [row, col - i]
            is_queen_left = True
        elif col - i < 0:
            queen_right = [row, 8 + col - i]
    if 0 <= row + i < 8 and 0 <= col + i < 8:
        if matrix[row + i][col + i] == 'Q' and not is_queen_prim_diag_down:
            queen_prim_diag_down = [row + i, col + i]
            is_queen_prim_diag_down = True
    if 0 <= row - i < 8 and 0 <= col - i < 8:
        if matrix[row - i][col - i] == 'Q' and not is_queen_prim_diag_up:
            queen_prim_diag_up = [row - i, col - i]
            is_queen_prim_diag_up = True
    if 0 <= row + i < 8 and 0 <= (col - i) < 8:
        if matrix[row + i][col - i] == 'Q' and not is_queen_second_diag_down:
            queen_second_diag_down = [row + i, col - i]
            is_queen_second_diag_down = True
    if 0 <= row - i < 8 and 0 <= col + i < 8:
        if matrix[row - i][col + i] == 'Q' and not is_queen_second_diag_up:
            queen_second_diag_up = [row - i, col + i]
            is_queen_second_diag_up = True


if queen_up:
    print(queen_up)
if queen_down:
    print(queen_down)
if queen_right:
    print(queen_right)
if queen_left:
    print(queen_left)
if queen_prim_diag_up:
    print(queen_prim_diag_up)
if queen_prim_diag_down:
    print(queen_prim_diag_down)
if queen_second_diag_up:
    print(queen_second_diag_up)
if queen_second_diag_down:
    print(queen_second_diag_down)
if not queen_up and not queen_down and not queen_right and not queen_left and not queen_prim_diag_up and not queen_prim_diag_down and not queen_second_diag_up and not queen_second_diag_down:
    print('The king is safe!')