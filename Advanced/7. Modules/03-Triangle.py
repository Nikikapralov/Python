from triangling import triangle
matrix = triangle(int(input()))
[print(' '.join([str(x) for x in line])) for line in matrix]
