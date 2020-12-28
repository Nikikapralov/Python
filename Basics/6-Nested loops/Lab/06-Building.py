number_of_floors = int(input())
number_of_doors = int(input())
for i in range(number_of_floors, 0, -1):
    for n in range(number_of_doors):
        if i == (number_of_floors):
            print(f'L{i}{n}', end=" ")
        elif i % 2 == 0:
            print(f'O{i}{n}', end=" ")
        elif i % 2 == 1:
            print(f'A{i}{n}', end=" ")
    print()
