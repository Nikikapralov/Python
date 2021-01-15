sugar_cubes = [int(sugar_cube) for sugar_cube in input().split()]

while True:
    command = input()
    if command == 'Mort':
        break
    command_split = command.split()
    if 'Add' in command_split:
        add_value = int(command_split[1])
        sugar_cubes.append(add_value)
    elif 'Remove' in command_split:
        remove_value = int(command_split[1])
        sugar_cubes.remove(remove_value)
    elif 'Replace' in command_split:
        replace_value = int(command_split[1])
        replacement = int(command_split[2])
        for index, value in enumerate(sugar_cubes):
            if value == replace_value:
                sugar_cubes[index] = replacement
                break
    elif 'Collapse' in command_split:
        collapse_value = int(command_split[1])
        sugar_cubes_collapse = []
        for index, value in enumerate(sugar_cubes):
            if value >= collapse_value:
                sugar_cubes_collapse.append(value)
                sugar_cubes = sugar_cubes_collapse
sugar_cubes_str = [str(item) for item in sugar_cubes]
output = ' '.join(sugar_cubes_str)
print(output)
