groceries = input().split('!')
while True:
    command = input()
    if 'Go Shopping!' in command:
        break
    command_split = command.split()
    if 'Urgent' in command_split:
        item_add = command_split[1]
        if item_add in groceries:
            continue
        else:
            groceries.insert(0, item_add)
    elif 'Unnecessary' in command_split:
        item_remove = command_split[1]
        if item_remove in groceries:
            groceries.remove(item_remove)
    elif 'Correct' in command_split:
        item_old = command_split[1]
        item_new = command_split[2]
        if item_old in groceries:
            index = groceries.index(item_old)
            groceries[index] = item_new
    elif 'Rearrange' in command_split:
        item_rearrange = command_split[1]
        if item_rearrange in groceries:
            groceries.remove(item_rearrange)
            groceries.append(item_rearrange)
groceries_final = ', '.join(groceries)
print(groceries_final)