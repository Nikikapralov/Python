matrix = [[int(x) for x in line.split()] for line in input().split('|')]
matrix = matrix[::-1]
print(' '.join([str(x) for line in matrix for x in line]))
