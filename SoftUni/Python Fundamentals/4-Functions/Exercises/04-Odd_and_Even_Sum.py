number = input()


def odd_and_even_sum(number):
    sum_even = 0
    sum_odd = 0
    for digit in number:
        int_digit = int(digit)
        if int_digit % 2 == 0:
            sum_even += int_digit
        elif int_digit % 2 == 1:
            sum_odd += int_digit
    sum_odd_print = f'Odd sum = {sum_odd}'
    sum_even_print = f'Even sum = {sum_even}'
    return str(sum_odd_print) + ',' + ' ' + str(sum_even_print)

execute = odd_and_even_sum(number)

print(execute)