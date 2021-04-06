def type_check(data):
    def decorator(function):
        def wrapper(number):
            if not isinstance(number, data):
                return 'Bad Type'
            result = function(number)
            return result
        return wrapper
    return decorator
