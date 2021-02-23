def add_and_subtract():
    number_1 = int(input())
    number_2 = int(input())
    number_3 = int(input())

    def sum_1_2(number_1, number_2):
        global result
        result = number_1 + number_2
        return result

    def subtract(result, number_3):
        global final
        final = result - number_3
        return final

    result = sum_1_2(number_1, number_2)
    final = subtract(result, number_3)

    return final


execute = add_and_subtract()
print(execute)
