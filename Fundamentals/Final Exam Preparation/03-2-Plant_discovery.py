n_plants = int(input())
plants = {}
for _ in range(n_plants):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    if plant not in plants:
        plants[plant] = [rarity, []]
    elif plant in plants:
        plants[plant][0] = rarity
while True:
    command = input()
    if command == 'Exhibition':
        break
    elif 'Rate' in command:
        placeholder = command.split()
        plant = placeholder[1]
        if plant in plants:
            rating = int(placeholder[3])
            plants[plant][1].append(rating)
        else:
            print('error')
    elif 'Update' in command:
        placeholder = command.split()
        plant = placeholder[1]
        if plant in plants:
            new_rarity = int(placeholder[3])
            plants[plant][0] = new_rarity
        else:
            print('error')
    elif 'Reset' in command:
        placeholder = command.split()
        plant = placeholder[1]
        if plant in plants:
            plants[plant][1].clear()
            plants[plant][1].append(0)

        else:
            print('error')
    else:
        print('error')
for item in plants:
    if plants[item][1]:
        plants[item][1] = (sum(plants[item][1]) / len(plants[item][1]))
    else:
        plants[item][1] = 0
print('Plants for the exhibition:')
for key, value in sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1])):
    print(f'- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}')

