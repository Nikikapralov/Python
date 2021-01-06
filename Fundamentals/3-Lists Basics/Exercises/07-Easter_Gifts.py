gifts = input().split()
while True:
    command = input()
    if command == 'No Money':
        break
    split_command = command.split()
    if 'OutOfStock' in split_command:
        for index, value in enumerate(gifts):
            if value == split_command[1]:
                gifts[index] = 'None'
    if 'Required' in split_command:
        int_number = int(split_command[2])
        if 0 <= int_number < len(gifts) - 1:
            gifts[int_number] = split_command[1]
        else:
            continue
    if 'JustInCase' in split_command:
        gifts[(len(gifts)) - 1] = split_command[1]
for x in range(len(gifts)):
    if gifts[x] == 'None':
        continue
    else:
        print(gifts[x], end=" ")
