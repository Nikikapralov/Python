from collections import deque
effects = deque([int(x) for x in input().split(', ')])
powers = [int(x) for x in input().split(', ')]
Palm = 0
Willow = 0
Crossette = 0

while True:
    if Palm == 3 and Willow == 3 and Crossette == 3:
        break
    if not effects or not powers:
        break
    effect = effects.popleft()
    power = powers.pop()
    sum_of_both = power + effect
    if effect <= 0:
        powers.append(power)
        continue
    elif power <= 0:
        effects.appendleft(effect)
        continue
    if sum_of_both % 3 == 0 and sum_of_both % 5 != 0:
        Palm += 1

    elif sum_of_both % 5 == 0 and sum_of_both % 3 != 0:
        Willow += 1

    elif sum_of_both % 5 == 0 and sum_of_both % 3 == 0:
        Crossette += 1

    else:
        effect -= 1
        effects.append(effect)
        powers.append(power)

if Palm >= 3 and Willow >= 3 and Crossette >= 3:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can’t make the perfect firework show.")
if effects:
    print(f'Firework Effects left: {", ".join([str(x) for x in effects])}')
if powers:
    print(f'Explosive Power left: {", ".join([str(x) for x in powers])}')
print(f'Palm Fireworks: {Palm}')
print(f'Willow Fireworks: {Willow}')
print(f'Crossette Fireworks: {Crossette}')


