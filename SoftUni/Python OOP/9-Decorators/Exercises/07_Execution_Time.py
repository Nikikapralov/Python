import time

def exec_time(function):
    def wrapper(*args):
        start = time.time()
        function(*args)
        end = time.time()
        result = end - start
        return result
    return wrapper




@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))
