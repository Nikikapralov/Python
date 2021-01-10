def perfect_number(number):
    not_so_perfect = "It's not so perfect."
    if number <= 0:
        return not_so_perfect
    while True:
        sum_of_divisers = 0
        for potential_diviser in range(1, number):
            if number % potential_diviser == 0:
                sum_of_divisers += potential_diviser
        if sum_of_divisers == number:
            perfect_number_print = 'We have a perfect number!'
            return perfect_number_print
        else:
            return not_so_perfect


number = int(input())
execute = perfect_number(number)
print(execute)