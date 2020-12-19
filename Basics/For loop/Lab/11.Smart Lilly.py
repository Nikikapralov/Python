age = int(input())
price_of_laundry = float(input())
price_per_toy = int(input())
sum_of_toys = 0
sum_of_money = 0
money_from_toys = 0
total_money = 0
leftover_money = 0
money_needed = 0

for i in range(1, age + 1):
    is_year_odd_or_even = i % 2 == 0
    if is_year_odd_or_even:
        sum_of_money += ((i // 2) * 10) - 1
    else:
        sum_of_toys += 1

money_from_toys = sum_of_toys * price_per_toy
total_money = money_from_toys + sum_of_money
leftover_money = total_money - price_of_laundry
money_needed = price_of_laundry - total_money

if total_money >= price_of_laundry:
    print(f'Yes! {leftover_money:.2f}')
else:
    print(f'No! {money_needed:.2f}')
