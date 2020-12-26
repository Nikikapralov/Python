type_flower = input()
amount = int(input())
budget = int(input())
price_roses = amount * 5
price_dahlias = amount * 3.80
price_tulips = amount * 2.80
price_narcissus = amount * 3
price_gladiolus = amount * 2.5
if type_flower == 'Roses' and amount > 80:
    price_roses -= price_roses * 0.1
    money_left = budget - price_roses
    if money_left >= 0:
        print(f"Hey, you have a great garden with {amount} {type_flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")


elif type_flower == 'Roses' and amount <= 80:
    money_left = budget - price_roses
    if money_left >= 0:
        print(f"Hey, you have a great garden with {amount} {type_flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")


elif type_flower == 'Dahlias' and amount > 90:
    price_dahlias -= price_dahlias * 0.15
    money_left = budget - price_dahlias
    if money_left >= 0:
        print(f"Hey, you have a great garden with {amount} {type_flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")


elif type_flower == 'Dahlias' and amount <= 90:
    money_left = budget - price_dahlias
    if money_left >= 0:
        print(f"Hey, you have a great garden with {amount} {type_flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")


elif type_flower == 'Tulips' and amount > 80:
    price_tulips -= price_tulips * 0.15
    money_left = budget - price_tulips
    if money_left >= 0:
        print(f"Hey, you have a great garden with {amount} {type_flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")


elif type_flower == 'Tulips' and amount <= 80:
    money_left = budget - price_tulips
    if money_left >= 0:
        print(f"Hey, you have a great garden with {amount} {type_flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")


elif type_flower == 'Narcissus' and amount < 120:
    price_narcissus += price_narcissus * 0.15
    money_left = budget - price_narcissus
    if money_left >= 0:
        print(f"Hey, you have a great garden with {amount} {type_flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")


elif type_flower == 'Narcissus' and amount >= 120:
    money_left = budget - price_narcissus
    if money_left >= 0:
        print(f"Hey, you have a great garden with {amount} {type_flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")


elif type_flower == 'Gladiolus' and amount < 80:
    price_gladiolus += price_gladiolus * 0.20
    money_left = budget - price_gladiolus
    if money_left >= 0:
        print(f"Hey, you have a great garden with {amount} {type_flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")


elif type_flower == 'Gladiolus' and amount >= 80:
    money_left = budget - price_gladiolus
    if money_left >= 0:
        print(f"Hey, you have a great garden with {amount} {type_flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
