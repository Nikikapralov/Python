def fibonacci():
    last = 0
    current = 0
    while True:
        if current == 0:
            yield current
            current += 1
        yield current
        current += last
        margin = current - last
        last = margin

