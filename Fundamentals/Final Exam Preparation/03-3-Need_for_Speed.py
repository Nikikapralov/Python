n_cars = int(input())
cars_dict = {}
for _ in range(n_cars):
    car, mileage, fuel = input().split('|')
    if car in cars_dict:
        continue
    elif car not in cars_dict:
        cars_dict[car] = [int(mileage)], [int(fuel)]
command = input()
while command != 'Stop':
    command_data = command.split(' : ')
    if command_data[0] == 'Drive':
        car = command_data[1]
        distance = int(command_data[2])
        fuel_needed = int(command_data[3])
        current_fuel = int(cars_dict[car][1][0])
        current_mileage = int(cars_dict[car][0][0])
        if fuel_needed <= current_fuel:
            current_fuel -= fuel_needed
            cars_dict[car][1][0] = int(current_fuel)
            print(f'{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.')
            current_mileage += distance
            cars_dict[car][0][0] = int(current_mileage)
            if current_mileage >= 100000:
                cars_dict.pop(car)
                print(f'Time to sell the {car}!')
        elif fuel_needed > current_fuel:
            print(f'Not enough fuel to make that ride')
    elif command_data[0] == 'Refuel':
        car = command_data[1]
        refuel = int(command_data[2])
        current_fuel = int(cars_dict[car][1][0])
        MAX_FUEL = 75
        new_fuel_total = current_fuel + refuel
        if new_fuel_total > MAX_FUEL:
            fuel_left = new_fuel_total - MAX_FUEL
            actual_fuel_used = refuel - fuel_left
            new_fuel_total = MAX_FUEL
        elif new_fuel_total <= MAX_FUEL:
            actual_fuel_used = refuel
        cars_dict[car][1][0] = int(new_fuel_total)
        print(f'{car} refueled with {actual_fuel_used} liters')
    elif command_data[0] == 'Revert':
        car = command_data[1]
        kilometers = int(command_data[2])
        current_mileage = int(cars_dict[car][0][0])
        new_mileage = current_mileage - kilometers
        if new_mileage <= 10000:
            new_mileage = 10000
            cars_dict[car][0][0] = int(new_mileage)
        else:
            cars_dict[car][0][0] = int(new_mileage)
            print(f'{car} mileage decreased by {kilometers} kilometers')

    command = input()

for key, value in sorted(cars_dict.items(), key=lambda x: (-x[1][0][0], x[0])):
    print(f'{key} -> Mileage: {value[0][0]} kms, Fuel in the tank: {value[1][0]} lt.')

