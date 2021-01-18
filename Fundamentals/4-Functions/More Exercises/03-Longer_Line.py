amount_of_points = 4


def find_distance(x, y):
    z_quadr = x**2 + y**2
    return z_quadr


def find_closer_to_0(points_a_b):
    distances = {}
    for current_point in points_a_b:
        x = current_point[0]
        y = current_point[1]
        distance = find_distance(x, y)
        x = int(x)
        y = int(y)
        current_points_x_y = (x, y)
        distances[current_points_x_y] = distance
    sorted_distances = sorted(distances.items(), key=lambda x: x[1], reverse=False)
    point_1 = sorted_distances[0][0]
    try:
        point_2 = sorted_distances[1][0]
    except IndexError:
        point_2 = point_1
    return point_1, point_2


def get_all_points():
    points = []
    for _ in range(amount_of_points // 2):
        curr_points = []
        for _ in range(amount_of_points // 2):
            x = float(input())
            y = float(input())
            curr_points.append((x, y))
        points.append(curr_points)
    return points


"Builds a trapezoid and gets the length by the formula for area."


def construct_small_triangle_inside_trapezoid(a, b, h):
    x = b - a
    y = h
    length = find_distance(x, y)
    return length


def get_length(point_a, point_b):
    a = point_a[1]
    b = point_b[1]
    h = abs(point_a[0]) + abs(point_b[0])
    length = construct_small_triangle_inside_trapezoid(a, b, h)
    return length


def find_longer_line(points):
    lengths = {}
    for line in range(len(points)):
        length = get_length(*points[line])
        lengths[line] = {'points': points[line], 'length': length}
    sorted_lengths = sorted(lengths.items(), key=lambda x: x[1]['length'], reverse=True)
    points_of_longest = sorted_lengths[0][1]['points']
    return points_of_longest


points = get_all_points()
points_of_longer_line = find_longer_line(points)
starting_point, ending_point = find_closer_to_0(points_of_longer_line)
print(starting_point, ending_point, sep='')