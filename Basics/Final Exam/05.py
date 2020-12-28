import sys
number_of_bees = int(input())
health_of_bear = int(input())
attack_of_bear= int(input())
health_of_bees = number_of_bees
attack_of_bees = number_of_bees * 5

while True:
    number_of_bees -= attack_of_bear #bear attacks
    attack_of_bees = number_of_bees * 5
    if number_of_bees < 100:
        if number_of_bees <= 0:
            print(f'The bear stole the honey! Bees left 0.')
            break
        print(f'The bear stole the honey! Bees left {number_of_bees}.')
        break
    health_of_bear -= attack_of_bees #bees attack
    if health_of_bear <= 0:
        print(f'Beehive won! Bees left {number_of_bees}.')
        break

