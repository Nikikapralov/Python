def even_parameters(function):

    def wrapper(*args):
        if [item for item in args if not isinstance(item, int)] or [num for num in args if num % 2 != 0]:
            return 'Please use only even numbers!'
        result = function(*args)
        return result

    return wrapper






@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
