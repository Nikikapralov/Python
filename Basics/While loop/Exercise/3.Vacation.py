amount_of_money_needed = float(input())
amount_of_money_she_currently_has = float(input())
amount_of_concurrent_days_she_spends_cash = 0
total_days = 0
while True:
    was_last_action_was_spend = 0
    save_or_spend = input()
    amount_spent_or_saved = float(input())
    total_days += 1
    if save_or_spend == 'spend':
        was_last_action_was_spend = 1
        amount_of_money_she_currently_has -= amount_spent_or_saved
        if amount_spent_or_saved > amount_of_money_she_currently_has:
            amount_of_money_she_currently_has = 0
    if was_last_action_was_spend == 1:
        amount_of_concurrent_days_she_spends_cash += 1
    if amount_of_concurrent_days_she_spends_cash == 5:
        print("You can't save the money.")
        print(f'{total_days}')
        break
    if save_or_spend == 'save':
        amount_of_concurrent_days_she_spends_cash = 0
        amount_of_money_she_currently_has += amount_spent_or_saved
    if amount_of_money_she_currently_has >= amount_of_money_needed:
        print(f'You saved the money for {total_days} days.')
        break





