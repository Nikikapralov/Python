bees = int(input())
flowers = int(input())
amount_of_honey = flowers * bees * 0.21
honey_plates = amount_of_honey // 100
honey_left = amount_of_honey % 100
print(f'{honey_plates:.0f} honeycombs filled.')
print(f'{honey_left:.2f} grams of honey left.')