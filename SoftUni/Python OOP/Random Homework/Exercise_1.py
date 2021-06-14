"""Create the class Person which will have the desired attributes."""


class Person:
    def __init__(self, height, weight, age, IQ, ID):
        self.height = height
        self.weight = weight
        self.age = age
        self.IQ = IQ
        self.ID = ID


"""Create the class PersonList which will have an array of people (self.people). Every time we add a person,
he will go into the array self.people We add individual people with the Controller class. Below more info.
"""


class PersonList:
    def __init__(self):
        self.people = []


"""Create the controller class. It is responsible for every action we want to do. Add people to the PersonList, get
data etc. The controller receives a person_list_object which is an instance of PersonList. Basically a list of people."""


class Controller:
    def __init__(self, person_list_object):
        self.person_list_object = person_list_object

    """Add a new person to the PersonList object."""

    def add_person(self, person_object):
        self.person_list_object.people.append(person_object)

    """Collect and sort the data."""

    def collect_data(self, criteria, flag=None):
        """We need to check if the desired criteria is available. We have a list of available criteria.
        If the criteria we want to order the data by is inside the array, we continue. If not, we print a message
        that the criteria is unavailable and end the program."""

        available_criteria = ['height', 'weight', 'age', 'IQ']
        if criteria not in available_criteria:
            print('Criteria not available!')
            return

        """We hold the data in a dictionary with key = ID and value = criteria. ID is necessary to differentiate between
        the individual people. 90, 100, 110 is ordered but not clear. Tom: 90, Jerry: 100, Rig: 110 is better. Our ID is
        numbers, in our case Tom is 1, Jerry is 2 and Rig is 3. 1:90, 2:100, 3:110."""
        data = {}
        """For every person in the PersonList, get the data. Person.weight will return the weight. We need to use getattr() though.
        Getattr(person, criteria(weight in our case))"""
        for person in self.person_list_object.people:
            data[person.ID] = getattr(person, criteria)

        """Flag can be "reversed" or empty. If the flag is 'reversed', the data will be returned in reversed order. 110, 100, 90."""
        """If no flag is given, the default flag is None and the data will be ordered from bottom up. 90, 100, 110"""
        if flag == 'reversed':
            ordered_data = sorted(data.items(), key=lambda x: (-x[1], x[0]))

        elif flag is None:
            ordered_data = sorted(data.items(), key=lambda x: (x[1], x[0]))

        """Print the ordered_data."""
        for key, value in ordered_data:
            print(f'ID: {key}, {criteria}: {value}')
        return

"""Create 3 people with their data, create a PersonList and a Controller which should receive the PersonList.
Then add the people to the PersonList. Finally choose a criteria on which to collect the data and a flag (reversed) if you
wish for it to be reversed. A non existent criteria will print an error message."""

person_1 = Person(1.80, 60, 10, 300, 1)
person_2 = Person(1.90, 30, 15, 10, 2)
person_3 = Person(0.30, 40, 54, 90, 3)
person_list = PersonList()
controller = Controller(person_list)

controller.add_person(person_1)
controller.add_person(person_2)
controller.add_person(person_3)
controller.collect_data('weight', 'reversed')
print('-' * 30)
controller.collect_data('weight')
print('-' * 30)
controller.collect_data('name')
print('-' * 30)
controller.collect_data('IQ', 'reversed')




