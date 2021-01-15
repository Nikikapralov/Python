def absolute(values):
    values_float = [float(x) for x in values]
    absolute_values = [abs(x) for x in values_float]
    return absolute_values


print(absolute(input().split()))
