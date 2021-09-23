def some_recursive(array, function):
    if not array:
        return False
    if function(array.pop()):
        return True
    return some_recursive(array, function)


def is_odd(num):
    if num%2==0:
        return False
    else:
        return True

print(some_recursive([2, 4], is_odd))