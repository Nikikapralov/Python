number_of_numbers = int(input())
sUm = 0
max_number = -9999999999999999999999999999999999
if number_of_numbers > 0:
    for i in range(1, number_of_numbers + 1):
        number = int(input())
        sUm += number
        if number > max_number:
            max_number = number
    sUm -= max_number
    if max_number == sUm:
        print('Yes')
        print(f'Sum = {sUm}')

    else:
        difference = abs(max_number - sUm)
        print('No')
        print(f'Diff = {difference}')
