import re
value_type_fire = input()
result = re.split(rf'[ =#]', value_type_fire)
value_type_fire_final = []
effort = 0
fire_put_out = 0
cells_put_out = []
for index1, value1 in enumerate(result):
    if value1 != '':
        value_type_fire_final.append(result[index1])
water = int(input())
while True:
    fire_type = 0
    counter = 0
    level = 0
    if water == 0:
        break
    if len(value_type_fire_final) == 0:
        break
    for value in value_type_fire_final:
        Flag = False
        if 'High' in value:
            fire_type = 'High'
        elif 'Medium' in value:
            fire_type = 'Medium'
        elif 'Low' in value:
            fire_type = 'Low'
        else:
            value = int(value)
            level = value
        if fire_type == 'High':
            if 81 <= level <= 125:
                counter += 1
                if water - level < 0:
                    continue
                else:
                    water -= level
                    fire_put_out += level
                    effort += 0.25 * level
                    cells_put_out.append(level)
            else:
                counter += 1
        elif fire_type == 'Medium':
            if 51 <= level <= 80:
                counter += 1
                if water - level < 0:
                    continue
                else:
                    water -= level
                    fire_put_out += level
                    effort += 0.25 * level
                    cells_put_out.append(level)
            else:
                counter += 1
        elif fire_type == 'Low':
            if 1 <= level <= 50:
                counter += 1
                if water - level < 0:
                    continue
                else:
                    water -= level
                    fire_put_out += level
                    effort += 0.25 * level
                    cells_put_out.append(level)
            else:
                counter += 1
        else:
            continue
        if counter == 2:
            break
    for n in range(2):
        value_type_fire_final.pop(0)
print('Cells:')
for x in cells_put_out:
    print(f'- {x}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {fire_put_out}')