board_size = int(input())
board = []
total_knights = []
all_knights = 0
total_kills = 0
for _ in range(board_size):
    board.append([x for x in input()])


def how_many_can_k_hit(board, row, col):
    knights = 0

    if (0 <= (row - 2) < len(board)) and 0 <= (col - 1) < len(board):
        up_left = board[row - 2][col - 1]
        if row >= 0 and col >= 0:
            if up_left == 'K':
                knights += 1

    if (0 <= (row - 2) < len(board)) and 0 <= (col + 1) < len(board):
        up_right = board[row - 2][col + 1]
        if up_right == 'K':
            knights += 1

    if (0 <= (row + 2) < len(board)) and 0 <= (col - 1) < len(board):
        down_left = board[row + 2][col - 1]
        if down_left == 'K':
            knights += 1

    if (0 <= (row + 2) < len(board)) and 0 <= (col + 1) < len(board):
        down_right = board[row + 2][col + 1]
        if down_right == 'K':
            knights += 1

    if (0 <= (row - 1) < len(board)) and 0 <= (col - 2) < len(board):
        left_up = board[row - 1][col - 2]
        if left_up == 'K':
            knights += 1

    if (0 <= (row + 1) < len(board)) and 0 <= (col - 2) < len(board):
        left_down = board[row + 1][col - 2]
        if left_down == 'K':
            knights += 1

    if (0 <= (row - 1) < len(board)) and 0 <= (col + 2) < len(board):
        right_up = board[row - 1][col + 2]
        if right_up == 'K':
            knights += 1

    if (0 <= (row + 1) < len(board)) and 0 <= (col + 2) < len(board):
        right_down = board[row + 1][col + 2]
        if right_down == 'K':
            knights += 1
    return knights


for row in range(board_size):
    for col in range(board_size):
        if board[row][col] == 'K':
            all_knights += 1
            total_knights.append((row, col))


while True:
    most_kills = 0
    to_kill = []
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 'K':
                result = how_many_can_k_hit(board, row, col)
                if result > most_kills:
                    most_kills = result
                    to_kill = [row, col]

    if most_kills == 0:
        break
    board[to_kill[0]][to_kill[1]] = '0'
    total_kills += 1
print(total_kills)