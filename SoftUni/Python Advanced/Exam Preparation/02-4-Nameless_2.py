word = list(input())
size = int(input())
matrix = [list(input()) for line in range(size)]
turns = int(input())

player_position = [(row, col) for row in range(size) for col in range(size) if matrix[row][col] == 'P']

for turn in range(turns):
    direction = input()
    row = player_position[0][0]
    col = player_position[0][1]

    if direction == 'up':
        if 0 <= row - 1 < size and 0 <= col < size:
            potential_letter = matrix[row - 1][col]
            matrix[row][col] = '-'
            if potential_letter != '-':
                word.append(potential_letter)
            player_position = [(row - 1, col)]
            matrix[row - 1][col] = 'P'
        else:
            if word:
                word.pop()

    elif direction == 'down':
        if 0 <= row + 1 < size and 0 <= col < size:
            potential_letter = matrix[row + 1][col]
            matrix[row][col] = '-'
            if potential_letter != '-':
                word.append(potential_letter)
            player_position = [(row + 1, col)]
            matrix[row + 1][col] = 'P'
        else:
            if word:
                word.pop()

    elif direction == 'right':
        if 0 <= row < size and 0 <= col + 1 < size:
            potential_letter = matrix[row][col + 1]
            matrix[row][col] = '-'
            if potential_letter != '-':
                word.append(potential_letter)
            player_position = [(row, col + 1)]
            matrix[row][col + 1] = 'P'
        else:
            if word:
                word.pop()

    elif direction == 'left':
        if 0 <= row < size and 0 <= col - 1 < size:
            potential_letter = matrix[row][col - 1]
            matrix[row][col] = '-'
            if potential_letter != '-':
                word.append(potential_letter)
            player_position = [(row, col - 1)]
            matrix[row][col - 1] = 'P'
        else:
            if word:
                word.pop()

print(''.join(word))
[print(''.join(line)) for line in matrix]

