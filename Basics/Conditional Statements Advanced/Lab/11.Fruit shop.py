fruit = input()
day = input()
amount = float(input())

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    price_banana = amount * 2.50
    price_apple = amount * 1.20
    price_orange = amount * 0.85
    price_grapefruit = amount * 1.45
    price_kiwi = amount * 2.70
    price_pineapple =  amount * 5.50
    price_grapes = amount * 3.85
    if fruit == 'banana':
        print(f'{price_banana:.2f}')
    elif fruit == 'apple':
        print(f'{price_apple:.2f}')
    elif fruit == 'orange':
        print(f'{price_orange:.2f}')
    elif fruit == 'grapefruit':
        print(f'{price_grapefruit:.2f}')
    elif fruit == 'kiwi':
        print(f'{price_kiwi:.2f}')
    elif fruit == 'pineapple':
        print(f'{price_pineapple:.2f}')
    elif fruit == 'grapes':
        print(f'{price_grapes:.2f}')
    else:
        print('error')

elif day == 'Saturday' or day == 'Sunday':
    price_banana = amount * 2.70
    price_apple = amount * 1.25
    price_orange = amount * 0.90
    price_grapefruit = amount * 1.60
    price_kiwi = amount * 3.00
    price_pineapple = amount * 5.60
    price_grapes = amount * 4.20

    if fruit == 'banana':
        print(f'{price_banana:.2f}')
    elif fruit == 'apple':
        print(f'{price_apple:.2f}')
    elif fruit == 'orange':
        print(f'{price_orange:.2f}')
    elif fruit == 'grapefruit':
        print(f'{price_grapefruit:.2f}')
    elif fruit == 'kiwi':
        print(f'{price_kiwi:.2f}')
    elif fruit == 'pineapple':
        print(f'{price_pineapple:.2f}')
    elif fruit == 'grapes':
        print(f'{price_grapes:.2f}')
    else:
        print('error')

else:
    print('error')
