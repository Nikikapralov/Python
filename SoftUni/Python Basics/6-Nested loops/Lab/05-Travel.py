from sys import exit
total_money = 0
while True:
    destination = input()
    if destination == 'End':
        exit()
    minimal_budget = float(input())
    total_money = 0
    while True:
        money_saved = float(input())
        total_money += money_saved
        if total_money >= minimal_budget:
            print(f'Going to {destination}!')
            break

