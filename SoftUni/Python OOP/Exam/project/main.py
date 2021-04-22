from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository


controller = Controller()
print(controller.add_aquarium('FreshwaterAquarium', 'a'))
print(controller.add_aquarium('SaltwaterAquarium', 'b'))
print(controller.add_fish('b', 'FreshwaterFish', 'brr', 'brr2', 10))
print(controller.add_fish('b', 'SaltwaterFish', 'brr', 'brr2', 10))
print(controller.add_decoration('Plant'))
print(controller.add_decoration('Ornament'))
print(controller.add_decoration('adasda'))
print(controller.feed_fish('a'))
print(controller.report())
print(controller.calculate_value('b'))
print(controller.insert_decoration('a', 'Plant'))
print(controller.insert_decoration('a', 'Plant'))
print(controller.insert_decoration('a', 'Ornament'))
