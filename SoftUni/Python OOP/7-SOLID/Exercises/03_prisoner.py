from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def walk_north(self, dist):
        pass

    @abstractmethod
    def walk_east(self, dist):
        pass


class FreePerson(Person):
    def __init__(self, *args):
        super().__init__(*args)

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        self.position = self.PRISON_LOCATION
        self.is_free = False

    def walk_north(self, dist):
        pass

    def walk_east(self, dist):
        pass


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")
