from sys import maxsize
from collections import deque


def compute_pureness(list_ints):
    pureness = 0
    for index, value in enumerate(list_ints):
        pureness += index * value
    list_ints.appendleft(list_ints.pop())
    return pureness


def best_list_pureness(*args):
    highest_number = -maxsize
    rotation_for_highest_n = None
    list_ints = deque([int(x) for x in args[0]])
    rotations = int(args[1])
    for rotation in range(rotations + 1):
        pureness = compute_pureness(list_ints)
        if pureness > highest_number:
            highest_number = pureness
            rotation_for_highest_n = rotation
    result = f'Best pureness {highest_number} after {rotation_for_highest_n} rotations'
    return result


test = ([2, 9, 1], 1)
result = best_list_pureness(*test)
print(result)
