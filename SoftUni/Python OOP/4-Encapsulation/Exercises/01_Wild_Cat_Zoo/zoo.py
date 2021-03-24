from lion import Lion
from cheetah import Cheetah
from tiger import Tiger
from keeper import Keeper
from caretaker import Caretaker
from vet import Vet


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def __get_string_animals_type(self, type_animal):
        animals = [animal for animal in self.animals if type(animal) == type_animal]
        result = f'----- {len(animals)} {type_animal.__class__.__name__}s:\n'
        for index in range(len(animals) - 1):
            animal = animals[index]
            result += f'{animal.__repr__()}\n'
        animal = animals[-1]
        result += f'{animal.__repr__()}'
        return result

    def __get_string_workers_type(self, type_worker):
        workers = [worker for worker in self.workers if type(worker) == type_worker]
        result = f'----- {len(workers)} {type_worker.__class__.__name__}s:\n'
        for index in range(len(workers) - 1):
            worker = workers[index]
            result += f'{worker.__repr__()}\n'
        worker = workers[-1]
        result += f'{worker.__repr__()}'
        return result

    def __adjust_budget(self, amount, sign):
        if sign == '-':
            self.__budget -= amount
        elif sign == '+':
            self.__budget += amount

    def __get_sum_money_animals(self):
        money = [animal.get_needs() for animal in self.animals]
        return sum(money)

    def __get_sum_worker_salaries(self):
        salaries = [worker.salary for worker in self.workers]
        return sum(salaries)

    def __check_budget(self, price):
        if self.__budget >= price:
            return True

    def __check_capacity_animals(self):
        if self.__animal_capacity > len(self.animals):
            return True

    def __check_capacity_workers(self):
        if self.__workers_capacity > len(self.workers):
            return True

    def __check_for_worker_with_name(self, worker_name):
        worker = [worker for worker in self.workers if worker.name == worker_name]
        return worker[0]

    def add_animal(self, animal, price):
        sign = '-'
        if not self.__check_budget(price) and self.__check_capacity_animals():
            return f'Not enough budget'
        if self.__check_capacity_animals() and self.__check_budget(price):
            self.animals.append(animal)
            self.__adjust_budget(price, sign)
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        return f'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__check_capacity_workers():
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return f'Not enough space for worker'

    def fire_worker(self, worker_name):
        worker = self.__check_for_worker_with_name(worker_name)
        if worker:
            self.workers.remove(worker)
            return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        sign = '-'
        to_pay = self.__get_sum_worker_salaries()
        if self.__check_budget(to_pay):
            self.__adjust_budget(to_pay, sign)
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        sign = '-'
        to_pay = self.__get_sum_money_animals()
        if self.__check_budget(to_pay):
            self.__adjust_budget(to_pay, sign)
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        sign = '+'
        self.__adjust_budget(amount, sign)

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        result += self.__get_string_animals_type(Lion)
        result += '\n'
        result += self.__get_string_animals_type(Tiger)
        result += '\n'
        result += self.__get_string_animals_type(Cheetah)
        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        result += self.__get_string_workers_type(Keeper)
        result += '\n'
        result += self.__get_string_workers_type(Caretaker)
        result += '\n'
        result += self.__get_string_workers_type(Vet)
        return result



