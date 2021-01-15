board_size = int(input())
board = []
total_knights = []
all_knights = 0
for _ in range(board_size):
    board.append([x for x in input()])

def how_many_can_k_hit(board, row, col):
    knights = 0

    if (0 <= (row - 2) < len(board)) and (0 <= (col - 1) < len(board)):
        up_left = board[row - 2][col - 1]
        if up_left == 'K':
            knights += 1

    if (0 <= (row - 2) < len(board)) and (0 <= (col + 1) < len(board)):
        up_right = board[row - 2][col + 1]
        if up_right == 'K':
            knights += 1

    if (0 <= (row + 2) < len(board)) and (0 <= (col - 1) < len(board)):
        down_left = board[row + 2][col - 1]
        if down_left == 'K':
            knights += 1

    if (0 <= (row + 2) < len(board)) and (0 <= (col + 1) < len(board)):
        down_right = board[row + 2][col + 1]
        if down_right == 'K':
            knights += 1

    if (0 <= (row - 1) < len(board)) and (0 <= (col - 2) < len(board)):
        left_up = board[row - 1][col - 2]
        if left_up == 'K':
            knights += 1

    if (0 <= (row + 1) < len(board)) and (0 <= (col - 2) < len(board)):
        left_down = board[row + 1][col - 2]
        if left_down == 'K':
            knights += 1

    if (0 <= (row - 1) < len(board)) and (0 <= (col + 2) < len(board)):
        right_up = board[row - 1][col + 2]
        if right_up == 'K':
            knights += 1

    if (0 <= (row + 1) < len(board)) and (0 <= (col + 2) < len(board)):
        right_down = board[row + 1][col + 2]
        if right_down == 'K':
            knights += 1
    return knights


def check_largest():
    global total_knights
    coordinates_of_knights = {}
    n = 1
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 'K':
                result = how_many_can_k_hit(board, row, col)
                coordinates_of_knights[n] = [row, col, result]
                n += 1
    largest = sorted(coordinates_of_knights.items(), key=lambda x: (x[1][2], -x[1][0], -x[1][1]))
    #[print(x) for x in largest]
    #print(f'999999999999999999999999999999999999999999999999999999999999999999999')
    number, values = largest.pop()
    row_1 = values[0]
    col_1 = values[1]
    kills = values[2]
    if kills == 0:
        return
    else:
        board[row_1][col_1] = '0'
        total_knights.pop()
        check_largest()


for row in range(board_size):
    for col in range(board_size):
        if board[row][col] == 'K':
            all_knights += 1
            total_knights.append((row, col))

check_largest()
print(all_knights - len(total_knights))

