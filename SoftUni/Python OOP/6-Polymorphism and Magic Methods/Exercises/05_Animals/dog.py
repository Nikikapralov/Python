from project.animal import Animal


class Dog(Animal):
    def __init__(self, *args):
        super().__init__(*args)

    def make_sound(self):
        return f'Woof!'