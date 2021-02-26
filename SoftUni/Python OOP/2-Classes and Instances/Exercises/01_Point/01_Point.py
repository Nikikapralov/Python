from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        distance = sqrt((self.x - x)**2 + (self.y - y)**2)
        return distance
