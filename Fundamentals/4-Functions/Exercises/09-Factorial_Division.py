def factorials(number_1, number_2):
    factorial_n1 = 1
    factorial_n2 = 1
    for number in range(1, number_1 + 1):
        factorial_n1 *= number
    for nmbr in range(1, number_2 + 1):
        factorial_n2 *= nmbr
    result = factorial_n1 / factorial_n2
    result = f'{result:.2f}'
    return result

number_1 = int(input())
number_2 = int(input())
execute = factorials(number_1=number_1, number_2=number_2)
print(execute)
