days = int(input())
room = input()
grade = input()

if room == 'room for one person':
    price = (days - 1) * 18
    if grade == 'negative':
        price = price - price * 0.1
        print(f'{price:.2f}')
    elif grade == 'positive':
        price += price * 0.25
        print(f'{price:.2f}')

elif room == 'apartment':
    price = (days - 1) * 25
    if days < 10:
        price -= price * 0.3
        if grade == 'negative':
            price -= price * 0.1
            print(f'{price:.2f}')
        elif grade == 'positive':
            price += price * 0.25
            print(f'{price:.2f}')

    elif days >= 10 and days <= 15:
        price -= price * 0.35
        if grade == 'negative':
            price -= price * 0.1
            print(f'{price:.2f}')
        elif grade == 'positive':
            price += price * 0.25
            print(f'{price:.2f}')

    elif days > 15:
        price -= price * 0.5
        if grade == 'negative':
            price -= price * 0.1
            print(f'{price:.2f}')
        elif grade == 'positive':
            price += price * 0.25
            print(f'{price:.2f}')

elif room == 'president apartment':
    price = (days - 1) * 35
    if days < 10:
        price -= price * 0.1
        if grade == 'negative':
            price -= price * 0.1
            print(f'{price:.2f}')
        elif grade == 'positive':
            price += price * 0.25
            print(f'{price:.2f}')

    elif days >= 10 and days <= 15:
        price -= price * 0.15
        if grade == 'negative':
            price -= price * 0.1
            print(f'{price:.2f}')
        elif grade == 'positive':
            price += price * 0.25
            print(f'{price:.2f}')

    elif days > 15:
        price -= price * 0.2
        if grade == 'negative':
            price -= price * 0.1
            print(f'{price:.2f}')
        elif grade == 'positive':
            price += price * 0.25
            print(f'{price:.2f}')
