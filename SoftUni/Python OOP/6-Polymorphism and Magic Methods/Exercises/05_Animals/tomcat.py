from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = 'Male'

    def make_sound(self):
        return 'Hiss'
