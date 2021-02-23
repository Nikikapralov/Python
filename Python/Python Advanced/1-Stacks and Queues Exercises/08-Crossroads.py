from collections import deque
green_light = int(input())
free_window = int(input())
queue_of_cars = deque()
cars_passed = 0
while True:
    current_green_light = green_light
    car = input()
    if car == 'END':
        break
    elif car == 'green':
        while current_green_light > 0 and queue_of_cars:
            current_car = queue_of_cars.popleft()
            current_green_light -= len(current_car)
            if current_green_light <= 0:
                seconds_needed = abs(current_green_light)
                if free_window >= seconds_needed:
                    cars_passed += 1
                    break
                else:
                    crash_point = seconds_needed - free_window
                    print(f'A crash happened!')
                    print(f'{current_car} was hit at {current_car[-crash_point]}.')
                    exit()
            else:
                cars_passed += 1
                continue
    else:
        queue_of_cars.append(car)
print('Everyone is safe.')
print(f'{cars_passed} total cars passed the crossroads.')
