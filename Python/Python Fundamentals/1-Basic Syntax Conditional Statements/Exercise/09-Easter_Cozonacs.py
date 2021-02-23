budget = float(input())
price_1kg_flour = float(input())
price_eggs = price_1kg_flour * 0.75
price_1l_milk = price_1kg_flour * 1.25
price_250ml_milk = price_1l_milk / 4
cozonac_count = 0
coloured_eggs = 0
money_left = 0
original_budget = budget
price_1_cozonac = price_1kg_flour + price_250ml_milk + price_eggs
while True:
    budget = budget - price_1_cozonac
    if budget < 0:
        break
    elif budget == 0:
        cozonac_count += 1
        coloured_eggs += 3
        break
    cozonac_count += 1
    coloured_eggs += 3
    if cozonac_count % 3 == 0:
        coloured_eggs -= cozonac_count - 2
money_left = original_budget - (cozonac_count * price_1_cozonac)
print(f'You made {cozonac_count} cozonacs! Now you have {coloured_eggs} eggs and {money_left:.2f}BGN left.')
