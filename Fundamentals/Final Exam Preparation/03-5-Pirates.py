command = input()
cities_dict = {}
while command != 'Sail':
    town, people, gold = command.split('||')
    if town not in cities_dict:
        cities_dict[town] = [int(people), int(gold)]
    elif town in cities_dict:
        people_1 = cities_dict[town][0] + int(people)
        gold_1 = cities_dict[town][1] + int(gold)
        cities_dict[town] = [people_1, gold_1]
    command = input()
while True:
    command = input()
    if command == 'End':
        break
    else:
        data = command.split('=>')
        if data[0] == 'Plunder':
            town = data[1]
            people = int(data[2])
            gold = int(data[3])
            print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
            new_people = cities_dict[town][0] - people
            new_gold = cities_dict[town][1] - gold
            if new_people == 0 or new_gold == 0:
                print(f'{town} has been wiped off the map!')
                cities_dict.pop(town)
                continue
            cities_dict[town][0] = new_people
            cities_dict[town][1] = new_gold
        elif data[0] == 'Prosper':
            town = data[1]
            gold = int(data[2])
            if gold < 0:
                print(f'Gold added cannot be a negative number!')
                continue
            new_gold = cities_dict[town][1] + gold
            cities_dict[town][1] = new_gold
            print(f'{gold} gold added to the city treasury. {town} now has {new_gold} gold.')
if len(cities_dict) == 0:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
print(f'Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:')
for key, value in sorted(cities_dict.items(), key=lambda x: (-x[1][1], x[0])):
    print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')