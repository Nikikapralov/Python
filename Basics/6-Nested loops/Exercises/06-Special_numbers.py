N = int(input())
for number_between_the_given_range in range(1111, 10000):
    number_in_str = str(number_between_the_given_range)
    is_modulo = 0
    result = 0
    is_magical_number = False
    for digit, value_of_digit in enumerate(number_in_str):
        value = int(value_of_digit)
        if value == 0:
            break
        is_modulo = N % value
        if not is_modulo:
            result += 1
            if result == 4:
                is_magical_number = True
                break
            continue
        else:
            break
    if is_magical_number:
        print(number_between_the_given_range, end=' ')


