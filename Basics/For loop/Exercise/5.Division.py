amount_of_numbers = int(input())
numbers_at_2 = 0
numbers_at_3 = 0
numbers_at_4 = 0
percent_2 = 0
percent_3 = 0
percent_4 = 0

for i in range(amount_of_numbers):
    number = int(input())
    if number % 2 == 0:
        numbers_at_2 += 1
    if number % 3 == 0:
        numbers_at_3 += 1
    if number % 4 == 0:
        numbers_at_4 += 1

percent_2 = numbers_at_2 / amount_of_numbers * 100
percent_3 = numbers_at_3 / amount_of_numbers * 100
percent_4 = numbers_at_4 / amount_of_numbers * 100

print(f'{percent_2:.2f}%')
print(f'{percent_3:.2f}%')
print(f'{percent_4:.2f}%')