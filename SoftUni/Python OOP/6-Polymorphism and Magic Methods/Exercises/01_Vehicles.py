from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    @abstractmethod
    def increase_fuel_consumption(self, amount):
        pass

    @abstractmethod
    def can_travel(self, distance):
        pass


class Car(Vehicle):
    SUMMER = 0.9

    def __init__(self, *args):
        super().__init__(*args)
        self.increase_fuel_consumption(Car.SUMMER)

    def increase_fuel_consumption(self, amount):
        self.fuel_consumption += amount

    def drive(self, distance):
        if distance <= 0:
            return
        fuel_needed = self.can_travel(distance)
        if fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def can_travel(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed <= self.fuel_quantity:
            return fuel_needed
        return False


class Truck(Vehicle):
    SUMMER = 1.6
    HOLE = 0.95

    def __init__(self, *args):
        super().__init__(*args)
        self.increase_fuel_consumption(Truck.SUMMER)

    def increase_fuel_consumption(self, amount):
        self.fuel_consumption += amount

    def drive(self, distance):
        if distance <= 0:
            return
        fuel_needed = self.can_travel(distance)
        if fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        fuel = self.__tiny_hole(fuel, Truck.HOLE)
        self.fuel_quantity += fuel

    def can_travel(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed <= self.fuel_quantity:
            return fuel_needed
        return False

    @staticmethod
    def __tiny_hole(to_fuel, amount_kept):
        to_fuel *= amount_kept
        return to_fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.drive(-1)
print(truck.fuel_quantity)
