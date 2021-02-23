def rounding(numbers):
    numbers_float = [float(x) for x in numbers]
    rounded_numbers = [round(x) for x in numbers_float]
    return rounded_numbers


print(rounding(input().split()))