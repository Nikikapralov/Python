def read_next(*args):
    list_of_iters = args
    for iterable in list_of_iters:
        for item in iterable:
            yield str(item)

for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')


