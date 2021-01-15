class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name = name_of_zoo
        self.mammals = []
        self.birds = []
        self.fishes = []

    def add_animal(self, species, name_of_animal):
        if species == 'mammal':
            self.mammals.append(name_of_animal)
        elif species == 'bird':
            self.birds.append(name_of_animal)
        elif species == 'fish':
            self.fishes.append(name_of_animal)

    def get_info(self, end_species):
        if end_species == 'mammal':
            print(f"Mammals in {self.name}: {', '.join(self.mammals)}")
        elif end_species == 'fish':
            print(f"Fishes in {self.name}: {', '.join(self.fishes)}")
        elif end_species == 'bird':
            print(f"Birds in {self.name}: {', '.join(self.birds)}")
        __animals = len(self.birds) + len(self.mammals) + len(self.fishes)
        print(f'Total animals: {self.__animals}')


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
n = int(input())
for x in range(n):
    data = input().split()
    species_of_animal_in_data, animal_in_data = data
    zoo.add_animal(species_of_animal_in_data, animal_in_data)
end_species = input()
zoo.get_info(end_species)


