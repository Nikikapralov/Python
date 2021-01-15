def get_data():
    rows = int(input())
    board = [[int(x) for x in input().split()] for x in range(rows)]
    cols = [len(col) for col in board]
    commands = [[int(x) for x in command.split('-')] for command in input().split()]
    return board, commands, rows, cols[0]


def destroy_ships(board, commands, rows, cols):
    destroyed = 0
    for command in commands:
        row = command[0]
        col = command[1]
        if 0 <= row < rows and 0 <= col < cols:
            ship = board[row][col]
            if ship > 0:
                board[row][col] -= 1
                if board[row][col] == 0:
                    destroyed += 1
    return destroyed

board, commands, rows, cols = get_data()
print(destroy_ships(board, commands, rows, cols))
