
quantity = int(input())
days = int(input())
money = 0
spirit = 0
ornament = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
for today in range(1, days + 1):
    Flag = False
    if today % 11 == 0:
        quantity += 2
    if today % 2 == 0:
        money += quantity * ornament
        spirit += 5
    if today % 3 == 0:
        money += quantity * (tree_skirt + tree_garlands)
        spirit += 13
        Flag = True
    if today % 5 == 0:
        money += quantity * tree_lights
        spirit += 17
        if Flag:
            spirit += 30
    if today % 10 == 0:
        spirit -= 20
        money += tree_garlands + tree_skirt + tree_lights
if days % 10 == 0:
    spirit -= 30
print(f'Total cost: {money}')
print(f'Total spirit: {spirit}')
