from math import sqrt


def get_coordinates():
    x = float(input())
    y = float(input())
    return x, y


def find_distance(x, y):
    z_quadr = x**2 + y**2
    z = sqrt(z_quadr)
    return z


amount_points = 2
distances = {}
for _ in range(amount_points):
    x, y = get_coordinates()
    current_distance = find_distance(x, y)
    x = int(x)
    y = int(y)
    points = (x, y)
    distances[points] = current_distance
sorted_distances = sorted(distances.items(), key=lambda x: x[1], reverse=False)
print(sorted_distances[0][0])
