class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value):
        self.__endurance = value

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        self.__sprint = value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value
    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        self.__passing = value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value

    def __str__(self):
        result = f'Player: {self.__name}\n' \
                 f'Endurance: {self.__endurance}\n' \
                 f'Sprint: {self.__sprint}\n' \
                 f'Dribble: {self.__dribble}\n' \
                 f'Passing: {self.__passing}\n' \
                 f'Shooting: {self.__shooting}\n'
        return result





