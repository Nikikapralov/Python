from collections import deque
bomb_effects_deque = deque([int(x) for x in input().split(', ')])
bomb_casings_stack = [int(x) for x in input().split(', ')]
bombs_materials = {'Datura Bombs': 40, 'Cherry Bombs': 60, 'Smoke Decoy Bombs': 120}
bombs_ezio_has = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
bombs_needed = 3
lower_casing_rating = 5


def is_pouch_filled(bomb_pouch, bombs_needed):
    for value in bomb_pouch.values():
        if value >= bombs_needed:
            continue
        else:
            return False
    return True


while True:
    current_effect = bomb_effects_deque.popleft()
    current_casing = bomb_casings_stack.pop()
    result = current_casing + current_effect
    if result in bombs_materials.values():
        for key, value in bombs_materials.items():
            if result == value:
                bombs_ezio_has[key] += 1
    else:
        bomb_effects_deque.appendleft(current_effect)
        current_casing -= lower_casing_rating
        bomb_casings_stack.append(current_casing)
    is_filled = is_pouch_filled(bombs_ezio_has, bombs_needed)
    if is_filled:
        break
    if not bomb_casings_stack or not bomb_effects_deque:
        break

if is_filled:
    print("Bene! You have successfully filled the bomb pouch!")
elif not is_filled:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects_deque:
    print(f'Bomb Effects: {", ".join([str(effect) for effect in bomb_effects_deque])}')
else:
    print(f'Bomb Effects: empty')

if bomb_casings_stack:
    print(f'Bomb Casings: {", ".join([str(casing) for casing in bomb_casings_stack])}')
else:
    print(f'Bomb Casings: empty')

for key, value in sorted(bombs_ezio_has.items(), key=lambda x: x[0]):
    print(f'{key}: {value}')





