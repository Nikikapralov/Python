class ValueCannotBeNegative(Exception):
    def __init__(self, value):
        message = f'Value cannot be negative! ({value})'
        super(ValueCannotBeNegative, self).__init__(message)


def read_numbers(size=5):
    numbers = []
    for number in range(size):
        curr_number = int(input())
        if curr_number < 0:
            raise ValueCannotBeNegative(curr_number)
        numbers.append(str(curr_number))
    return " ".join(numbers)


print(read_numbers())