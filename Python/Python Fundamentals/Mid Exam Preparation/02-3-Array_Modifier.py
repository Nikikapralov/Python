array = [int(number) for number in input().split()]
while True:
    command = input()
    if command == 'end':
        break
    command_split = command.split()

    if 'swap' in command_split:
        swap_index_1 = int(command_split[1])
        swap_index_2 = int(command_split[2])
        array[swap_index_1], array[swap_index_2] = array[swap_index_2], array[swap_index_1]
    elif 'multiply' in command_split:
        multiply_index_1 = int(command_split[1])
        multiply_index_2 = int(command_split[2])
        item_1 = array[multiply_index_1]
        item_2 = array[multiply_index_2]
        array[multiply_index_1] = item_1 * item_2
    elif 'decrease' in command_split:
        for index in range(len(array)):
            array[index] -= 1
array_str = [str(x) for x in array]
output = ', '.join(array_str)
print(output)
