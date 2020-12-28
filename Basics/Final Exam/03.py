flower_type = input()
amount_of_flower = int(input())
season = input()
honey_from_sunflower = 0
honey_from_daisy = 0
honey_from_lavender = 0
honey_from_mint = 0

if season == 'Spring':
    honey_from_sunflower = 10 * amount_of_flower
    honey_from_daisy = 12 * amount_of_flower
    honey_from_lavender = 12 * amount_of_flower
    honey_from_mint = 10 * amount_of_flower
    honey_from_daisy += 0.1 * honey_from_daisy
    honey_from_mint += 0.1 * honey_from_mint

elif season == 'Autumn':
    honey_from_sunflower = 12 * amount_of_flower
    honey_from_daisy = 6 * amount_of_flower
    honey_from_lavender = 6 * amount_of_flower
    honey_from_mint = 6 * amount_of_flower
    honey_from_sunflower -= 0.05 * honey_from_sunflower
    honey_from_daisy -= 0.05 * honey_from_daisy
    honey_from_lavender  -= 0.05 * honey_from_lavender
    honey_from_mint -= 0.05 * honey_from_mint

elif season == 'Summer':
    honey_from_sunflower = 8 * amount_of_flower
    honey_from_daisy = 8 * amount_of_flower
    honey_from_lavender = 8 * amount_of_flower
    honey_from_mint = 12 * amount_of_flower
    honey_from_sunflower += 0.1 * honey_from_sunflower
    honey_from_daisy += 0.1 * honey_from_daisy
    honey_from_lavender += 0.1 * honey_from_lavender
    honey_from_mint += 0.1 * honey_from_mint

if flower_type == 'Sunflower':
    print(f'Total honey harvested: {honey_from_sunflower:.2f}')
elif flower_type == 'Daisy':
    print(f'Total honey harvested: {honey_from_daisy:.2f}')
elif flower_type == 'Lavender':
    print(f'Total honey harvested: {honey_from_lavender:.2f}')
elif flower_type == 'Mint':
    print(f'Total honey harvested: {honey_from_mint:.2f}')