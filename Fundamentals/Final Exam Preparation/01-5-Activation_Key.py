activation_key = input()

while True:
    command = input()
    if command == 'Generate':
        break
    else:
        data = command.split('>>>')
        if data[0] == 'Contains':
            substring = data[1]
            if substring in activation_key:
                print(f'{activation_key} contains {substring}')
            else:
                print(f'Substring not found!')
        elif data[0] == 'Flip':
            upper_or_lower = data[1]
            start_index = int(data[2])
            end_index = int(data[3])
            if upper_or_lower == 'Upper':
                upper = activation_key[start_index:end_index].upper()
                activation_key = activation_key[:start_index] + upper + activation_key[end_index:]
                print(activation_key)
            elif upper_or_lower == 'Lower':
                lower = activation_key[start_index:end_index].lower()
                activation_key = activation_key[:start_index] + lower + activation_key[end_index:]
                print(activation_key)
        elif data[0] == 'Slice':
            start_index = int(data[1])
            end_index = int(data[2])
            activation_key = activation_key[:start_index] + activation_key[end_index:]
            print(activation_key)
print(f'Your activation key is: {activation_key}')