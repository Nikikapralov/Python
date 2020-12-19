amount_of_numbers = int(input())
sum1 = 0
sum2 = 0
for i in range(1, amount_of_numbers + 1):
    number1 = int(input())
    if_i_is_odd_or_even = i % 2 == 0
    if if_i_is_odd_or_even:
        sum1 += number1
    else:
        sum2 += number1
difference = abs(sum1 - sum2)
if sum1 == sum2:
    print('Yes')
    print(f'Sum = {sum1}')
else:
    print('No')
    print(f'Diff = {difference}')