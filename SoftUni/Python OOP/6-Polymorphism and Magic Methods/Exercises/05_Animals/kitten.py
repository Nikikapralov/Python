from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = 'Female'

    def make_sound(self):
        return f'Meow'

