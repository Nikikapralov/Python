def genrange(start, end):
    current = start - 1
    while True:
        current += 1
        if current > end:
            break
        yield current

print(list(genrange(1, 10)))