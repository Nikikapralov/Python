rows, cols = [int(x) for x in input().split()]

letters = {x: y for x, y in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])}
matrix_1 = [[letters[row] + letters[row + col] + letters[row] for col in range(cols)] for row in range(rows)]
#matrix = []
#for row in range(rows):
    #line = []
    #for col in range(cols):
        #first_last = letters[row]
        #middle = letters[row + col]
        #word = first_last + middle + first_last
        #line.append(word)
    #matrix.append(line)
#[print(' '.join(x)) for x in matrix]

matrix_1 = [[letters[row] + letters[row + col] + letters[row] for col in range(cols)] for row in range(rows)]
[print(' '.join(x)) for x in matrix_1]
