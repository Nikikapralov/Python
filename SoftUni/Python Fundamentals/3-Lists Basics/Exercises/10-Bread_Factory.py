import sys
INITIAL_COINS = 100
INITIAL_ENERGY = 100
coins = INITIAL_COINS
energy = INITIAL_ENERGY
working_day_events = input().split('|')
for string in working_day_events:
    event, value = string.split('-')
    value = int(value)
    if event == 'rest':
        if energy + value >= 100:
            print('You gained 0 energy.')
            energy = 100
        else:
            energy += value
            print(f'You gained {value} energy.')
        print(f'Current energy: {energy}.')
    elif event == 'order':
        if energy - 30 < 0:
            energy += 50
            print(f'You had to rest!')
            continue
        else:
            coins += value
            energy -= 30
            print(f'You earned {value} coins.')
    else:
        if coins - value <= 0:
            print(f'Closed! Cannot afford {event}.')
            sys.exit()
        else:
            coins -= value
            print(f'You bought {event}.')
print('Day completed!')
print(f'Coins: {coins}')
print(f'Energy: {energy}')