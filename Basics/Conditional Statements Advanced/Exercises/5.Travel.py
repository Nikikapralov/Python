budget = float(input())
season = input()
money_spent = 0

if season == 'summer':
    if budget <= 100 and budget != 0:
        money_spent = budget * 0.3
        print('Somewhere in Bulgaria')
        print(f'Camp - {money_spent:.2f}')
    elif (budget <= 1000 and budget > 100) and budget != 0:
        money_spent = budget * 0.4
        print('Somewhere in Balkans')
        print(f'Camp - {money_spent:.2f}')
    elif budget > 1000 and budget != 0:
        money_spent = budget * 0.9
        print('Somewhere in Europe')
        print(f'Hotel - {money_spent:.2f}')

elif season == 'winter':
    if budget <= 100 and budget != 0:
        money_spent = budget * 0.7
        print('Somewhere in Bulgaria')
        print(f'Hotel - {money_spent:.2f}')
    elif (budget <= 1000 and budget) and budget != 0:
        money_spent = budget * 0.8
        print('Somewhere in Balkans')
        print(f'Hotel - {money_spent:.2f}')
    elif budget > 1000 and budget != 0:
        money_spent = budget * 0.9
        print('Somewhere in Europe')
        print(f'Hotel - {money_spent:.2f}')
