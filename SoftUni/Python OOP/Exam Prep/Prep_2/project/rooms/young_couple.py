from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = []
        self.__get_appliances()
        self.expenses = self.calculate_expenses(self.appliances)

    def __get_appliances(self):
        tv = self.members_count * TV()
        laptop = self.members_count * Laptop()
        fridge = self.members_count * Fridge()
        [self.appliances.append(obj) for obj in tv]
        [self.appliances.append(obj) for obj in laptop]
        [self.appliances.append(obj) for obj in fridge]
