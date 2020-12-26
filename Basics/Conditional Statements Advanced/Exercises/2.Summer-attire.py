degrees = int(input())
time_of_day = input()

if 10 <= degrees <=18:
    if time_of_day == 'Morning':
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif time_of_day == 'Afternoon':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif time_of_day == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
elif 18 < degrees <=24:
    if time_of_day == 'Morning':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f'It\'s {degrees} degrees, get your {Outfit} and {Shoes}.')
    elif time_of_day == 'Afternoon':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif time_of_day == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
elif degrees >= 25:
    if time_of_day == 'Morning':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif time_of_day == 'Afternoon':
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif time_of_day == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

