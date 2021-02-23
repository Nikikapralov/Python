amount_of_numbers = int(input())
sum1 = 0
sum2 = 0
for i in range(amount_of_numbers):
    number = int(input())
    sum1 += number
for i in range (amount_of_numbers):
    number2 = int(input())
    sum2 += number2

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
elif sum2 != sum1:
    difference = abs(sum1 - sum2)
    print(f'No, diff = {difference}')
