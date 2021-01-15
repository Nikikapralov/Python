import re
pattern = r'^>>(?P<item>\w+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)$'
bougth_items = []
total_price = 0
while True:
    command = input()
    if command == "Purchase":
        break
    else:
        data = command
        result = re.finditer(pattern, data)
        if result:
            for item in result:
                dictionary = item.groupdict()
                bougth_items.append(dictionary['item'])
                price = float(dictionary['price'])*int(dictionary['quantity'])
                total_price += price

        else:
            continue
print('Bought furniture:')
for item in bougth_items:
    print(item)
print(f'Total money spend: {total_price:.2f}')

r'^>>(?P<name>[a-zA-Z]+((\s[a-zA-Z0-9]+(\.[0-9]+)?)+)?[!]?)<<[0-9]+(\.[0-9]+)?![0-9]+$'
