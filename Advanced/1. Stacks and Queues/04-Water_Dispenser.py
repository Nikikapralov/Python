import collections
water_tank = int(input())
queque = collections.deque()
while True:
    name = input()
    if name == 'Start':
        break
    else:
        queque.append(name)

while True:
    command = input()
    if command.isdigit():
        liters = int(command)
        if water_tank >= liters:
            water_tank -= liters
            print(f'{queque.popleft()} got water')
        else:
            print(f'{queque.popleft()} must wait')
    elif 'refill' in command:
        useless, refill = command.split()
        water_tank += int(refill)
    elif command == 'End':
        break

print(f'{water_tank} liters left')

