size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for line in range(size)]
player_position = [(row, col) for row in range(size) for col in range(size) if matrix[row][col] == 'P']
total_coins = 0
game_over = False
coins_list = []

while True:
    if total_coins >= 100:
        break

    row = player_position[0][0]
    col = player_position[0][1]
    direction = input()

    if direction == 'up':
        if 0 <= row - 1 < size and 0 <= col < size:
            new_position = matrix[row - 1][col]
            if new_position == 'X':
                game_over = True
                break
            else:
                total_coins += new_position
                coins_list.append([row - 1, col])
                matrix[row - 1][col] = 'P'
                matrix[row][col] = 0
                player_position = [(row - 1, col)]
        else:
            game_over = True
            break

    elif direction == 'down':
        if 0 <= row + 1 < size and 0 <= col < size:
            new_position = matrix[row + 1][col]
            if new_position == 'X':
                game_over = True
                break
            else:
                total_coins += new_position
                coins_list.append([row + 1, col])
                matrix[row + 1][col] = 'P'
                matrix[row][col] = 0
                player_position = [(row + 1, col)]
        else:
            game_over = True
            break

    elif direction == 'right':
        if 0 <= row < size and 0 <= col + 1 < size:
            new_position = matrix[row][col + 1]
            if new_position == 'X':
                game_over = True
                break
            else:
                total_coins += new_position
                coins_list.append([row, col + 1])
                matrix[row][col + 1] = 'P'
                matrix[row][col] = 0
                player_position = [(row, col + 1)]

        else:
            game_over = True
            break

    elif direction == 'left':
        if 0 <= row < size and 0 <= col - 1 < size:
            new_position = matrix[row][col - 1]
            if new_position == 'X':
                game_over = True
                break
            else:
                total_coins += new_position
                coins_list.append([row, col - 1])
                matrix[row][col - 1] = 'P'
                matrix[row][col] = 0
                player_position = [(row, col - 1)]

        else:
            game_over = True
            break
    else:
        continue

if game_over:
    total_coins = int(total_coins / 2)
    print(f"Game over! You've collected {total_coins} coins.")
else:
    print(f"You won! You've collected {total_coins} coins.")
print(f'Your path:')
[print(x) for x in coins_list]
