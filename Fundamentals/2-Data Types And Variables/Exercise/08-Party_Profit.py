party_size = int(input())
days = int(input())
coins = 0
for current_day in range(1, days + 1):
    Flag = False
    coins += 50
    if current_day % 10 == 0:
        party_size -= 2
    if current_day % 15 == 0:
        party_size += 5
    coins -= party_size * 2
    if current_day % 3 == 0:
        coins -= party_size * 3
        Flag = True
    if current_day % 5 == 0:
        coins += 20 * party_size
        if Flag:
            coins -= party_size * 2
coins_per_companion = int(coins / party_size)
print(f'{party_size} companions received {coins_per_companion} coins each.')
