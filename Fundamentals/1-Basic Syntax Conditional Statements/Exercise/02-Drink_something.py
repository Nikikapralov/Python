age = int(input())
kid = 'toddy '
teen = 'coke '
young_adult = 'beer '
adult = 'whisky '
drink = 'drink '
if age <= 14:
    drink += kid
elif age <= 18:
    drink += teen
elif age <= 21:
    drink += young_adult
elif age > 21:
    drink += adult
print(drink)