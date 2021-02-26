import re
collection = input()
final_collection = re.split(r'[|\->]', collection)
for item in final_collection:
    if item == '':
        final_collection.remove(item)
budget = float(input())
price = 0
type_item = 0
counter = 0
upped_price = 0
upped_price_list = []
total_money_from_sell = 0
profit = 0
for index, value in enumerate(final_collection):
    upped_price = 0
    if index % 2 == 0:
        type_item = value
        counter += 1
    elif index % 2 == 1:
        price = float(value)
        counter += 1
    if counter == 2:
        counter = 0
        if budget < price:
            continue
        if type_item == 'Clothes' and 0 <= price <= 50:
            budget -= price
            upped_price = price + price * 0.4
            upped_price_list.append(upped_price)
            total_money_from_sell += upped_price
            profit += price * 0.4
        elif type_item == 'Shoes' and 0 <= price <= 35:
            budget -= price
            upped_price = price + price * 0.4
            upped_price_list.append(upped_price)
            total_money_from_sell += upped_price
            profit += price * 0.4
        elif type_item == 'Accessories' and 0 <= price <= 20.50:
            budget -= price
            upped_price = price + price * 0.4
            upped_price_list.append(upped_price)
            total_money_from_sell += upped_price
            profit += price * 0.4
        else:
            continue

for item in upped_price_list:
    print(f'{item:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if sum(upped_price_list) + budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
