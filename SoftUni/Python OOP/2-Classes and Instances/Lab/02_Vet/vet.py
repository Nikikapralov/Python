class Vet:
    animals = []  # total amount of animals for all vets
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []  # animals for current vet

    def register_animal(self, animal_name):
        if not self.space:
            return f'Not enough space'
        else:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            Vet.space -= 1
            return f'{animal_name} registered in the clinic'

    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f'{animal_name} not in the clinic'
        else:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            Vet.space += 1
            return f'{animal_name} unregistered successfully'

    def info(self):
        return f'{self.name} has {len(self.animals)} animals. {self.space} space left in clinic'
