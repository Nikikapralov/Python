def recursive_power(number, power):
    if power == 1:
        return number
    power -= 1
    number *= recursive_power(number, power)
    return number


print(recursive_power(2, 10))