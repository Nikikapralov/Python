def cache(func):

    def wrapper(n):
        result = func(n)
        wrapper.log[n] = result
        if result == 0:
            wrapper.log[result] = 0
        return result

    wrapper.log = {}
    return wrapper



@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
