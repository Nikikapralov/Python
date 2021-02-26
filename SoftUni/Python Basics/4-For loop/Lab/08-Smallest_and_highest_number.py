number_of_numbers = int(input())
min_number = 999999999999999999999999999999999999999999999999999999999999
max_number = -99999999999999999999999999999999999999999999999999999999999
for i in range(0, number_of_numbers):
    number = int(input())
    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
