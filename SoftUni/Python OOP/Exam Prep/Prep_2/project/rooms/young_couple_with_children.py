from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.appliances = []
        self.children = children
        self.__get_appliances()
        self.expenses = self.calculate_expenses(self.appliances, self.children)

    def __get_appliances(self):
        tv = self.members_count * TV()
        laptop = self.members_count * Laptop()
        fridge = self.members_count * Fridge()
        [self.appliances.append(obj) for obj in tv]
        [self.appliances.append(obj) for obj in laptop]
        [self.appliances.append(obj) for obj in fridge]