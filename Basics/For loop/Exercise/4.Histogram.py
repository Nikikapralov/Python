amount_of_numbers = int(input())
percent_below_200 = 0
percent_between_200_and_399 = 0
percent_between_400_and_599 = 0
percent_between_600_and_799 = 0
percent_above_800 = 0
amount_below_200 = 0
amount_between_200_and_399 = 0
amount_between_400_and_599 = 0
amount_between_600_and_799 = 0
amount_above_800 = 0
for i in range(amount_of_numbers):
    number = int(input())
    if number < 200:
        amount_below_200 += 1
    elif 200 <= number <= 399:
        amount_between_200_and_399 += 1
    elif 400 <= number <= 599:
        amount_between_400_and_599 += 1
    elif 600 <= number <= 799:
        amount_between_600_and_799 += 1
    elif number >= 800:
        amount_above_800 += 1

percent_below_200 = amount_below_200 / amount_of_numbers * 100
percent_between_200_and_399 = amount_between_200_and_399 / amount_of_numbers * 100
percent_between_400_and_599 = amount_between_400_and_599 / amount_of_numbers * 100
percent_between_600_and_799 = amount_between_600_and_799 / amount_of_numbers * 100
percent_above_800 = amount_above_800 / amount_of_numbers * 100

print(f'{percent_below_200:.2f}%')
print(f'{percent_between_200_and_399:.2f}%')
print(f'{percent_between_400_and_599:.2f}%')
print(f'{percent_between_600_and_799:.2f}%')
print(f'{percent_above_800:.2f}%')