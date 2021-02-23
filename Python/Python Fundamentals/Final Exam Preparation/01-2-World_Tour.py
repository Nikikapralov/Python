travel_info = input()
while True:
    command = input()
    if command == 'Travel':
        break
    elif 'Add' in command:
        add, data = command.split()
        stop, index, string = data.split(':')
        index = int(index)
        if index in range(len(travel_info)):
            new_travel_info = travel_info[:index] + string + travel_info[index:]
            travel_info = new_travel_info
    elif 'Remove' in command:
        remove, data = command.split()
        stop, start_index, end_index = data.split(':')
        start_index = int(start_index)
        end_index = int(end_index)
        if (start_index and end_index) in range(len(travel_info)):
            new_travel_info = travel_info[:start_index] + travel_info[end_index + 1:]
            travel_info = new_travel_info
    elif 'Switch' in command:
        switch, old_string, new_string = command.split(':')
        travel_info = travel_info.replace(old_string, new_string)
    print(travel_info)

print(f'Ready for world tour! Planned stops: {travel_info}')


