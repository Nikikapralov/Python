matrix = [[int(x) for x in input().split()] for line in range(int(input()))]
while True:
    curr_command = input()
    if curr_command == 'END':
        break
    command, row, col, number = curr_command.split()
    row = int(row)
    col = int(col)
    if command == 'Subtract':
        if 0 <= row < len(matrix) and 0 <= col < len(matrix):
            matrix[row][col] -= int(number)
        else:
            print('Invalid coordinates')
            continue
    elif command == 'Add':
        if 0 <= row < len(matrix) and 0 <= col < len(matrix):
            matrix[row][col] += int(number)
        else:
            print('Invalid coordinates')
            continue
[print(' '.join([str(x) for x in line])) for line in matrix]
