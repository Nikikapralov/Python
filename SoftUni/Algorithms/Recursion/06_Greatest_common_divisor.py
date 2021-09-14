def GCD(num_1, num_2):
    if num_1 >= num_2:
        bigger = num_1
        smaller = num_2
    else:
        bigger = num_2
        smaller = num_1
    if num_1 == 0:
        return num_2
    if num_2 == 0:
        return num_1
    return GCD(smaller, bigger % smaller)

print(GCD(15, 5))