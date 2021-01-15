size = 3


def get_board(size):
    board = [[x for x in input().split()] for line in range(size)]
    return board


def check_columns(board, size):
    for col in range(size):
        if all([board[row][col] == '1' for row in range(size)]):
            return 'First player won'
        elif all([board[row][col] == '2' for row in range(size)]):
            return 'Second player won'
    return None


def check_rows(board, size):
    for row in board:
        if all([x == '1' for x in row]):
            return 'First player won'
        elif all([x == '2' for x in row]):
            return 'Second player won'
    return None


def check_main_diag(board, size):
    if all([board[row][row] == '1' for row in range(size)]):
        return 'First player won'
    elif all([board[row][row] == '2' for row in range(size)]):
        return 'Second player won'
    return None

def check_secondary_diag(board, size):
    if all([board[row][size - row - 1] == '1' for row in range(size)]):
        return 'First player won'
    elif all([board[row][size - row - 1] == '2' for row in range(size)]):
        return 'Second player won'
    return None

def check_winner(board):
    winner = check_columns(board, size)
    if winner is not None:
        return winner
    winner = check_rows(board, size)
    if winner is not None:
        return winner
    winner = check_main_diag(board, size)
    if winner is not None:
        return winner
    winner = check_secondary_diag(board, size)
    if winner is not None:
        return winner
    return 'Draw!'


board = get_board(size)
print(check_winner(board))
