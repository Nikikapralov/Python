def calculate_factorial(n):
    assert n >= 1 and int(n) == n
    if n == 1:
        return n
    return n * calculate_factorial(n-1)

print(calculate_factorial(10))