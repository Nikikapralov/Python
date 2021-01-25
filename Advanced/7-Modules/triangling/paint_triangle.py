def triangle(size):
    matrix = []
    for row in range(1, size + 1):
        line = []
        start = 1
        for col in range(row):
            line.append(start)
            start += 1
        matrix.append(line)
    for row in range(size - 1, 0, -1):
        line = []
        start = 1
        for col in range(row):
            line.append(start)
            start += 1
        matrix.append(line)
    return matrix
