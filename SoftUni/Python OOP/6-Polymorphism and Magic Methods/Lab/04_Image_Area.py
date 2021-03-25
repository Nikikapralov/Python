class ImageArea:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def __gt__(self, other):
        if self.get_area() > other.get_area():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.get_area() >= other.get_area():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.get_area() < other.get_area():
            return True
        else:
            return False

    def __le__(self, other):
        if self.get_area() <= other.get_area():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.get_area() == other.get_area():
            return True
        else:
            return False

    def __ne__(self, other):
        if self.get_area() != other.get_area():
            return True
        else:
            return False

