budget = int(input())
season = input()
number_of_fishermen = int(input())
price = 0
is_odd_or_even = number_of_fishermen % 2 == 0

if season == 'Spring':
    price = 3000

elif season == 'Summer' or season == 'Autumn':
    price = 4200

elif season == 'Winter':
    price = 2600

if number_of_fishermen <= 6:
    price -= price * 0.1

elif number_of_fishermen >= 7 and number_of_fishermen <= 11:
    price -= price * 0.15

elif number_of_fishermen > 11:
    price -= price * 0.25

if (season == 'Spring' or season == 'Winter' or season == 'Summer') and is_odd_or_even:
    price -= price * 0.05

money_left = budget - price
if budget >= price:
    print(f'Yes! You have {money_left:.2f} leva left.')

elif budget < price:
    print(f'Not enough money! You need {abs(money_left):.2f} leva.')
