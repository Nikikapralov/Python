input = 10


def recursive_factorial(input):
    if input == 1:
        return input

    return input * recursive_factorial(input - 1)

print(recursive_factorial(input))