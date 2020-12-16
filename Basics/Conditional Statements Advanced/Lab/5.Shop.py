product = input()
town = input()
amount = float(input())

if town == 'Sofia':
    if product == 'coffee':
        price_coffee = amount * 0.50
        print(price_coffee)
    elif product == 'water':
        price_water = amount * 0.80
        print(price_water)
    elif product == 'beer':
        price_beer = amount * 1.20
        print(price_beer)
    elif product == 'sweets':
        price_sweets = amount * 1.45
        print(price_sweets)
    elif product == 'peanuts':
        price_peanuts = amount * 1.60
        print(price_peanuts)

elif town == 'Plovdiv':
    if product == 'coffee':
        price_coffee = amount * 0.40
        print(price_coffee)
    elif product == 'water':
        price_water = amount * 0.70
        print(price_water)
    elif product == 'beer':
        price_beer = amount * 1.15
        print(price_beer)
    elif product == 'sweets':
        price_sweets = amount * 1.30
        print(price_sweets)
    elif product == 'peanuts':
        price_peanuts = amount * 1.50
        print(price_peanuts)

elif town == 'Varna':
    if product == 'coffee':
        price_coffee = amount * 0.45
        print(price_coffee)
    elif product == 'water':
        price_water = amount * 0.70
        print(price_water)
    elif product == 'beer':
        price_beer = amount * 1.10
        print(price_beer)
    elif product == 'sweets':
        price_sweets = amount * 1.35
        print(price_sweets)
    elif product == 'peanuts':
        price_peanuts = amount * 1.55
        print(price_peanuts)