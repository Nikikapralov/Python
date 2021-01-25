from collections import deque


def get_players():
    players = {}
    print('Player one name:', end=' ')
    player_1 = input()
    players['player_1'] = {'name': player_1}
    print('Player two name:', end=' ')
    player_2 = input()
    players['player_2'] = {'name': player_2}
    return players


def ask_for_x_or_o(players):
    print(f'{players["player_1"]["name"]} would you like to play with "X" or with "O"?')
    while True:
        icon = input().upper()
        if icon != 'X' and icon != 'O':
            print('Please choose "X" or "O"')
            continue
        players['player_1'].update({'icon': icon})
        break
    if players['player_1']['icon'] == 'X':
        players['player_2'].update({'icon': 'O'})
    else:
        players['player_2'].update({'icon': 'X'})
    return players


def numerate_board():
    board = []
    n = 1
    for row in range(3):
        line = []
        for col in range(3):
            line.append(n)
            n += 1
        board.append(line)
    return board


def print_board(board):
    for line in board:
        [print(f'| {x} |', end=' ') for x in line]
        print()


def present_board_numeration():
    print(f'This is the numeration of the board:')
    board = numerate_board()
    print_board(board)
    return board


def empty_vs_enumerated(board):
    print(f'Would you like to play on an empty board? Or would you prefer to stay with enumerated?\n'
          f'Press 1 for empty, 2 for enumerated.', end=' ')
    while True:
        decision = input()
        if decision == '1':
            board = write_the_board_empty()
            print(f'This is your board now:')
            print_board(board)
            print(f'Choose 1 to continue or 2 to revert to enumerated!', end=' ')
            while True:
                decision = input()
                if decision == '1':
                    return board
                elif decision == '2':
                    board = numerate_board()
                    print(f'This is your board now:')
                    print_board(board)
                    return board
                else:
                    print(f'Choose 1 to continue or 2 to revert to enumerated!', end=' ')
                    continue
        elif decision == '2':
            print(f'The board above is your board!')
            return board

        else:
            print(f'Press 1 for empty, 2 for enumerated.', end=' ')
            continue


def write_the_board_empty():
    board = [[' ' for x in range(3)] for line in range(3)]
    return board


def define_starting_player(players):
    for player, nested_dict in players.items():
        for key, value in nested_dict.items():
            if key == 'icon':
                if value == 'X':
                    starting_player = player
    print(f'{players[starting_player]["name"]} starts first!')
    return starting_player


def make_the_deque(players, starting_player):
    players_deque = deque(players)
    while players_deque[0] != starting_player:
        current = players_deque.popleft()
        players_deque.append(current)
    return players_deque



def choose_position(deque_players, dev_board, board, players):
    current_player = deque_players.popleft()
    deque_players.append(current_player)
    spot_is_free = False
    print(f'{players[current_player]["name"]} choose a free position [1-9]:', end=' ')
    while True:
        try:
            position = int(input())
        except ValueError:
            print(f'Number please!')
            print_board(board)
            continue
        if position not in range(1, 10):
            print('Please enter a valid position!')
            print_board(board)
            continue
        for line in dev_board:
            if position not in line:
                continue
            else:
                spot_is_free = True
                break
        if not spot_is_free:
            print(f'Spot is taken! Choose another one!')
            print_board(board)
            continue
        else:
            for row in range(3):
                for col in range(3):
                    if dev_board[row][col] == position:
                        dev_board[row][col] = players[current_player]['icon']
                        board[row][col] = players[current_player]['icon']
                        return deque_players, dev_board, board

def find_winner(item, players):
    for player, nested_dict in players.items():
        for key_1, value_1 in nested_dict.items():
            if key_1 == 'icon':
                if value_1 == item:
                    winner = players[player]['name']
                    return winner, True


def check_row(row, players):
    if all([item == 'X' for item in row]):
        winner, someone_won = find_winner('X', players)
        return winner, someone_won
    elif all([item == 'O' for item in row]):
        winner, someone_won = find_winner('O', players)
        return winner, someone_won
    else:
        return None, False
 

def check_diagonal_one(board, players):
    if all([board[row][row] == 'X' for row in range(3)]):
        winner, someone_won = find_winner('X', players)
        return winner, someone_won
    elif all([board[row][row] == 'O' for row in range(3)]):
        winner, someone_won = find_winner('O', players)
        return winner, someone_won
    else:
        return None, False


def check_diagonal_two(board, players):
    if all([board[row][3 - row - 1] == 'X' for row in range(3)]):
        winner, someone_won = find_winner('X', players)
        return winner, someone_won
    elif all([board[row][3 - row - 1] == 'O' for row in range(3)]):
        winner, someone_won = find_winner('O', players)
        return winner, someone_won
    else:
        return None, False


def check_col(col, players, board):
    if all([board[row][col] == 'X' for row in range(3)]):
        winner, someone_won = find_winner('X', players)
        return winner, someone_won
    
    elif all([board[row][col] == 'O' for row in range(3)]):
        find_winner('O', players)
        winner, someone_won = find_winner('O', players)
        return winner, someone_won
    
    winner, someone_won = check_diagonal_one(board, players)
    if someone_won:
        return winner, someone_won

    winner, someone_won = check_diagonal_two(board, players)
    if someone_won:
        return winner, someone_won
    
    else:
        return None, False


def did_someone_win(board, players):
    for row in board:
        winner, someone_won = check_row(row, players)
        if someone_won:
            return winner, True

    for col in range(3):
        winner, someone_won = check_col(col, players, board)
        if someone_won:
            return winner, True

    else:
        return None, False



def playing(deque_players, dev_board, board, players):
    counter = 0
    while True:
        counter += 1
        deque_players, dev_board, board = choose_position(deque_players, dev_board, board, players)
        print_board(board)
        winner, someone_won = did_someone_win(board, players)
        if someone_won:
            print(f'Winner is: {winner}! Press 1 to play again, 2 to quit!', end=' ')
            play_again(players)

        elif counter == 9:
            print(f'No one wins! Press 1 to play again, 2 to quit!', end=' ')
            play_again(players)
        continue


def play_again(players):
    while True:
        try:
            command = int(input())
        except ValueError:
            print(f'Press 1 to play again or 2 to quit!', end=' ')
            continue
        if command == 1:
            print(f'You have chosen to play again! Same players? 1 for yes, 2 for no.')
            while True:
                try:
                    command = int(input())
                except ValueError:
                    print(f'Press 1 to play again with same players or 2 to play with new players!')
                if command == 1:
                    again(players)
                else:
                    main()
        else:
            exit()


def again(players):
    players = ask_for_x_or_o(players)
    board = present_board_numeration()
    board = empty_vs_enumerated(board)
    starting_player = define_starting_player(players)
    deque_players = make_the_deque(players, starting_player)
    dev_board = numerate_board()
    playing(deque_players, dev_board, board, players)



def main():
    players = get_players()
    players = ask_for_x_or_o(players)
    board = present_board_numeration()
    board = empty_vs_enumerated(board)
    starting_player = define_starting_player(players)
    deque_players = make_the_deque(players, starting_player)
    dev_board = numerate_board()
    playing(deque_players, dev_board, board, players)


main()