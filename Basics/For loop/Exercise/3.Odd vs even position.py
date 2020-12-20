number_of_numbers = int(input())
odd_min = 99999999999999999999999999999999999999
odd_max = -99999999999999999999999999999999999999
even_min = 9999999999999999999999999999999999999
even_max = -9999999999999999999999999999999999999
odd_sum = 0
even_sum = 0
if number_of_numbers != 0 and number_of_numbers != 1:
    for i in range(1, number_of_numbers + 1):
        number = float(input())
        is_odd_or_even = i % 2 == 0
        if is_odd_or_even:
            even_sum += number
            if number > even_max:
                even_max = number
            if number < even_min:
                even_min = number
        else:
            odd_sum += number
            if number > odd_max:
                odd_max = number
            if number < odd_min:
                odd_min = number
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')

elif number_of_numbers == 0:
    for i in range(1, number_of_numbers + 1):
        number = float(input())
        is_odd_or_even = i % 2 == 0
        if is_odd_or_even:
            even_sum += number
            if number > even_max:
                even_max = number
            if number < even_min:
                even_min = number
        else:
            odd_sum += number
            if number > odd_max:
                odd_max = number
            if number < odd_min:
                odd_min = number

    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')

elif number_of_numbers == 1:
    for i in range(1, number_of_numbers + 1):
        number = float(input())
        is_odd_or_even = i % 2 == 0
        if is_odd_or_even:
            even_sum += number
            if number > even_max:
                even_max = number
            if number < even_min:
                even_min = number
        else:
            odd_sum += number
            if number > odd_max:
                odd_max = number
            if number < odd_min:
                odd_min = number

    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')


