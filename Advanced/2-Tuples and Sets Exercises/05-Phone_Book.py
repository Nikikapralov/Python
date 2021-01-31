phonebook = {}
data = input()
while not data.isdigit():
    name, number = data.split('-')
    phonebook[name] = number
    data = input()
for _ in range(int(data)):
    current_name = input()
    if current_name in phonebook:
        print(f'{current_name} -> {phonebook[current_name]}')
    else:
        print(f'Contact {current_name} does not exist.')
