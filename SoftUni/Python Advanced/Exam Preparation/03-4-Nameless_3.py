def get_magic_triangle(size):
    size = int(size)
    triangle = [1]
    if size == 0:
        print(triangle)
        return triangle
    elif size == 1:
        triangle = [1]
        print(triangle)
        return triangle
    elif size == 2:
        triangle = [[1], [1, 1]]
        print(triangle)
        return triangle

    triangle = [[1], [1, 1]]
    for n in range(3, size + 1):
        new_line = [1]
        for index in range(0, len(triangle[-1]) - 1):
            to_append = triangle[-1][index] + triangle[-1][index + 1]
            new_line.append(to_append)
        new_line.append(1)
        triangle.append(new_line)
    return triangle