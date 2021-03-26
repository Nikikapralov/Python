from project.animal import Animal


class Cat(Animal):
    def __init__(self, *args):
        super().__init__(*args)

    def make_sound(self):
        return 'Meow meow!'
