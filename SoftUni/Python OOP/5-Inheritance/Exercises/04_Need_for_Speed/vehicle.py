class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = float(fuel)
        self.horse_power = horse_power

    def get_needed_fuel(self, kilometers):
        fuel_needed = kilometers * self.fuel_consumption
        return fuel_needed

    def enough_fuel(self, kilometers):
        fuel_needed = self.get_needed_fuel(kilometers)
        if fuel_needed <= self.fuel:
            return True
        return False

    def drive(self, kilometers):
        fuel_needed = self.get_needed_fuel(kilometers)
        if self.enough_fuel(kilometers):
            self.fuel -= fuel_needed


