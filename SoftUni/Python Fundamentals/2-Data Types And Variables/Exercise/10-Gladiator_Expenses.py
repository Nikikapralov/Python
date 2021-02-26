lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
cost_of_helmet = 0
cost_of_sword = 0
cost_of_shield = 0
cost_of_armor = 0
counter = 0
for game in range(1, lost_fights + 1):
    Flag = False
    if game % 2 == 0:
        cost_of_helmet += helmet_price
        Flag = True
    if game % 3 == 0:
        cost_of_sword += sword_price
        if Flag:
            cost_of_shield += shield_price
            counter += 1
    if counter == 2:
        cost_of_armor += armor_price
        counter = 0
expenses = cost_of_armor + cost_of_shield + cost_of_helmet + cost_of_sword
print(f'Gladiator expenses: {expenses:.02f} aureus')



