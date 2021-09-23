def recursive_range(number):
    if number == 1:
        return 1
    return number + recursive_range(number - 1)
print(recursive_range(6))