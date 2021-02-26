is_it_prime = True
sum_prime = 0
sum_not_prime = 0
while True:
    command = input()
    if command == 'stop':
        break
    number = int(command)
    if number < 0:
        print('Number is negative.')
        continue
    for i in range(2,number - 1):
        if number % i == 0:
            is_it_prime = False
            break
        else:
            is_it_prime = True
    if is_it_prime:
        sum_prime += number
    elif not is_it_prime:
        sum_not_prime += number
    if number == '1':
        sum_prime += 1
    elif number == '2':
        sum_prime += 2

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_not_prime}')



