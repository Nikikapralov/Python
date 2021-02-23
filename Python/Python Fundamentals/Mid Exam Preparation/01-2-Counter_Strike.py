import sys
initial_energy = int(input())
wins = 0

while True:
    distance = input()
    if distance == 'End of battle':
        break
    distance = int(distance)
    initial_energy -= distance
    if initial_energy >= 0:
        wins += 1
    elif initial_energy < 0:
        initial_energy += distance
        print(f'Not enough energy! Game ends with {wins} won battles and {initial_energy} energy')
        sys.exit()
    if wins % 3 == 0:
        initial_energy += wins

print(f'Won battles: {wins}. Energy left: {initial_energy}')


