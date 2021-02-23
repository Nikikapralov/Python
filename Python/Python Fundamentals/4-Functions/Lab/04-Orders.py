def price_of_order(item, quantity:int):
    price = None
    coffee = 1.50
    water = 1.00
    coke = 1.40
    snacks = 2.00
    if item == 'coffee':
        price = coffee * quantity
    elif item == 'water':
        price = water * quantity
    elif item == 'coke':
        price = coke * quantity
    elif item == 'snacks':
        price = snacks * quantity
    return price


item = input()
quantity = int(input())
result = price_of_order(item=item, quantity=quantity)
print(f'{result:.2f}')
