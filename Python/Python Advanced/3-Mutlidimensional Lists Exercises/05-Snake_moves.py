from collections import deque
rows, cols = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    matrix.append(['' for x in range(cols)])
snake = deque([x for x in input()])
for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            letter = snake.popleft()
            snake.append(letter)
            matrix[row][col] = letter
    else:
        for col in range(cols - 1, -1, -1):
            letter = snake.popleft()
            snake.append(letter)
            matrix[row][col] = letter

[print(''.join(x)) for x in matrix]
