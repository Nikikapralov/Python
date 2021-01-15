taxes = 0
total_price = 0
price = 0
final = 0
while True:
    price_or_customer_type = input()
    final = total_price + taxes
    if price_or_customer_type == 'special':
        final -= (total_price + taxes) * 0.1
        break
    elif price_or_customer_type == 'regular':
        break
    else:
        price = float(f'{float(price_or_customer_type):.2f}')
        if price < 0:
            print('Invalid price!')
            continue
        total_price += price
        taxes += price * 0.2

if final == 0:
    print('Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print(f'-----------')
    print(f'Total price: {final:.2f}$')
