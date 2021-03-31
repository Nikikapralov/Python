def squares(n, start=0):
    while True:
        start += 1
        if start > n:
            break
        yield start ** 2

print(list(squares(5)))