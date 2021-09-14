def calculate_digits_sum(n):
    assert n >= 0 and int(n) == n
    if n == 0:
        return n
    return n % 10 + calculate_digits_sum(n // 10)

print(calculate_digits_sum(40000))