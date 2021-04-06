def number_increment(numbers):

    def increase():
        numbers_2 = []

        for number in numbers:
            numbers_2.append(number + 1)

        return numbers_2

    return increase


print(number_increment([1, 2, 3])())