class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supply = [sup for sup in self.supplies if sup.__class__.__name__ == 'FoodSupply']
        if not food_supply:
            raise IndexError('There are no food supplies left!')
        return food_supply

    @property
    def water(self):
        water_supply = [sup for sup in self.supplies if sup.__class__.__name__ == 'WaterSupply']
        if not water_supply:
            raise IndexError('There are no water supplies left!')
        return water_supply

    @property
    def painkillers(self):
        pain_supply = [sup for sup in self.medicine if sup.__class__.__name__ == 'Painkiller']
        if not pain_supply:
            raise IndexError('There are no painkillers left!')
        return pain_supply

    @property
    def salves(self):
        salves_supply = [sup for sup in self.medicine if sup.__class__.__name__ == 'Salve']
        if not salves_supply:
            raise IndexError('There are no salves left!')
        return salves_supply

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            if medicine_type == 'Painkiller':
                medicine_remove = self.painkillers[-1]
            else:
                medicine_remove = self.salves[-1]
            self.medicine.remove(medicine_remove)
            medicine_remove.apply(survivor)
            return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            if sustenance_type == 'WaterSupply':
                sustenance = self.water.pop()
            else:
                sustenance = self.food.pop()
            self.supplies.remove(sustenance)
            sustenance.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            to_reduce = survivor.age * 2
            survivor.needs -= to_reduce
        for survivor in self.survivors:
            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')
