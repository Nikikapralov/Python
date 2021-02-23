dictionary = {key: {'item': [], 'Sum': 0} for key in input().split(', ')}
while True:
    command = input()
    if command == 'End':
        break
    name, item, price = command.split('-')
    if name in dictionary:
        if item in dictionary[name]['item']:
            continue
        dictionary[name]['item'].append(item)
        dictionary[name]['Sum'] += int(price)

[print(f'{key} -> Items: {len(value["item"])}, Cost: {value["Sum"]}') for key, value in dictionary.items()]
