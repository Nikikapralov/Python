daily_steps = 10000
total_amount_of_steps = 0
difference = 0
while True:
    amount_of_steps = input()
    if amount_of_steps == 'Going home':
        amount_of_steps = int(input())
        total_amount_of_steps += amount_of_steps
        difference = abs(daily_steps - total_amount_of_steps)
        if total_amount_of_steps >= daily_steps:
            print('Goal reached! Good job!')
            print(f'{difference} steps over the goal!')
            break
        if total_amount_of_steps < daily_steps:
            print(f'{difference} more steps to reach goal.')
            break

    amount_of_steps = int(amount_of_steps)
    total_amount_of_steps += amount_of_steps
    difference = abs(daily_steps - total_amount_of_steps)
    if total_amount_of_steps >= daily_steps:
        print('Goal reached! Good job!')
        print(f'{difference} steps over the goal!')
        break