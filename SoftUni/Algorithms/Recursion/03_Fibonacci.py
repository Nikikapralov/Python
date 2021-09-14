def fibonacci(n):
    assert n >= 0 and int(n) == n
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))