class Inventory:
    __capacity = None

    def __init__(self, __capacity):
        self.capacity = __capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        left_capacity = self.capacity - len(self.items)
        return f'Items: {", ".join(self.items)}.\nCapacity left: {left_capacity}'


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
inventory.capacity = 10
print(inventory.get_capacity())
