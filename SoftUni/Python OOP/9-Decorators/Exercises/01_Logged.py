def logged(function):
    def wrapper(*args):
        result = f'you called {function.__name__}{args}\n' \
                 f'it returned {function(*args)}'
        return result
    return wrapper


