dictionary = {key: {'quantity': 0, 'quality': 0, 'item': []} for key in input().split(', ')}
for _ in range(int(input())):
    category, item, quan_qual = input().split(' - ')
    quantity_num, quality_num = quan_qual.split(';')
    quantity, number_quan = quantity_num.split(':')
    quality, number_qual = quality_num.split(':')
    if category in dictionary:
        dictionary[category]['item'].append(item)
        dictionary[category]['quality'] += int(number_qual)
        dictionary[category]['quantity'] += int(number_quan)
print(f'Count of items: {sum([value["quantity"]for value in dictionary.values()])}')
print(f'Average quality: {(sum([value["quality"] for value in dictionary.values()]) / len(dictionary)):.2f}')
[print(f'{key} -> {", ".join([x for x in value["item"]])}') for key, value in dictionary.items()]
