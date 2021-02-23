items = input().split(', ')
while True:
    command = input().split(' - ')
    if 'Craft!' in command:
        break
    elif 'Collect' in command:
        if command[1] in items:
            continue
        else:
            items.append(command[1])
    elif 'Drop' in command:
        if command[1] in items:
            items.remove(command[1])
        else:
            continue
    elif 'Combine Items' in command:
        combine_items = command[1].split(':')
        if combine_items[0] in items:
            index = items.index(combine_items[0])
            items.insert(index + 1, combine_items[1])
        else:
            continue
    elif 'Renew' in command:
        if command[1] in items:
            items.remove(command[1])
            items.append(command[1])
result = ', '.join(items)
print(result)