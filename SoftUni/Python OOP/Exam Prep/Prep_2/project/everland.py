class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses * 30 + room.room_cost
        return f'Monthly consumption: {total_consumption:.2f}$.'

    def pay(self):
        result = []
        new_list = []
        for room in self.rooms:
            to_pay = room.room_cost + room.expenses * 30
            if room.budget >= to_pay:
                result.append(f'{room.family_name} paid {to_pay:.2f}$ and have {room.budget:.2f}$ left.')
                new_list.append(room)
            else:
                result.append(f'{room.family_name} does not have enough budget and must leave the hotel.')
        self.rooms = new_list
        return '\n'.join(result)

    def status(self):
        result = f'Total population: {sum([room.members_count for room in self.rooms])}\n'
        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. ' \
                      f'Budget: {room.budget:.2f}$, Expenses: {room.expenses * 30:.2f}$\n'
            if hasattr(room, 'children'):
                for child in room.children:
                    result += f'--- Child {room.children.index(child) + 1} monthly cost: {child.cost * 30:.2f}$\n'
            if self.rooms.index(room) == len(self.rooms) - 1:
                result += f'--- Appliances monthly cost: {sum([app.get_monthly_expense() for app in room.appliances]):.2f}$'
            else:
                result += f'--- Appliances monthly cost: {sum([app.get_monthly_expense() for app in room.appliances]):.2f}$\n'
        return result




