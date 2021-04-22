from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.stove import Stove
from project.appliances.fridge import Fridge


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        self.family_name = family_name
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = []
        self.__get_appliances()
        self.expenses = self.calculate_expenses(self.appliances)

    def __get_appliances(self):
        tv = self.members_count * TV()
        stove = self.members_count * Stove()
        fridge = self.members_count * Fridge()
        [self.appliances.append(obj) for obj in tv]
        [self.appliances.append(obj) for obj in stove]
        [self.appliances.append(obj) for obj in fridge]


