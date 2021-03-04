class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = int(capacity)
        self.items = {}

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'

    @classmethod
    def from_size(cls, name, type, size):
        capacity = size / 2
        return cls(name, type, capacity)

    def add_item(self, item_name):
        if item_name not in self.items:
            self.items[item_name] = 1
            return f'{item_name} added to the store'
        if self.items[item_name] < self.capacity:
            self.items[item_name] += 1
            return f'{item_name} added to the store'

        return f'Not enough capacity in the store'

    def remove_item(self, item_name, amount: int):
        if item_name not in self.items:
            return f'Cannot remove {amount} {item_name}'
        if self.items[item_name] < amount:
            return f'Cannot remove {amount} {item_name}'
        self.items[item_name] -= amount
        return f'{amount} {item_name} removed from the store'





