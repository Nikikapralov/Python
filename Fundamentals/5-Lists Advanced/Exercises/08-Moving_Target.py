import sys
target = [int(number) for number in input().split()]


def is_radius_valid(radius):
    global max_index
    global min_index
    max_index = index_strike + radius
    min_index = index_strike - radius
    if min_index < 0 or max_index < 0:
        return False
    if min_index in range(0, len(target)) and max_index in range(0, len(target)):
        return True
    else:
        return False


while True:
    command = [int(number_command) if number_command.isdigit() else number_command for number_command in input().split()]
    if 'End' in command:
        break
    elif 'Shoot' in command:
        index_shoot = int(command[1])
        power = int(command[2])
        if index_shoot in range(len(target)):
            target[index_shoot] -= power
            if target[index_shoot] <= 0:
                target.pop(index_shoot)

    elif 'Add' in command:
        index_add = int(command[1])
        value = int(command[2])
        if index_add in range(len(target)):
            target.insert(index_add, value)
        else:
            print('Invalid placement!')
    elif 'Strike' in command:
        index_strike = int(command[1])
        radius = int(command[2])
        if is_radius_valid(radius):
            for index in range(min_index, max_index + 1):
                target[index] = sys.maxsize
            while sys.maxsize in target:
                for number in target:
                    if number == sys.maxsize:
                        target.remove(number)
        else:
            print('Strike missed!')


target_str = [str(item) for item in target]
result = '|'.join(target_str)
print(result)