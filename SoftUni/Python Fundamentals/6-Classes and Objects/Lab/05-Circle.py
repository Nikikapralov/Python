class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        circumference = 2 * Circle.__pi * self.radius
        return circumference

    def calculate_area(self):
        area = Circle.__pi * (self.radius ** 2)
        return area

    def calculate_area_of_sector(self, angle):
        area_of_sector = (angle / 360) * Circle.__pi * (self.radius ** 2)
        return area_of_sector


diameter_circle_1 = 10
circle_1 = Circle(diameter_circle_1)
angle = 5

print(f"{circle_1.calculate_circumference():.2f}")
print(f"{circle_1.calculate_area():.2f}")
print(f"{circle_1.calculate_area_of_sector(angle):.2f}")
