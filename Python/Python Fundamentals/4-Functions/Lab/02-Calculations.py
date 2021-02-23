def calculation(number_1, number_2, operator):
    result = None
    if operator == 'subtract':
        result = number_1 - number_2
    elif operator == 'add':
        result = number_1 + number_2
    elif operator == 'multiply':
        result = number_1 * number_2
    elif operator == 'divide':
        result = number_1 // number_2
    return result


operator = input()
number_1 = int(input())
number_2 = int(input())
print(calculation(number_1, number_2, operator))
