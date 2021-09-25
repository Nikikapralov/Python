def allFib(n):
    for i in range(n):
        print(str(i)+":, " + str(fib(i)))

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


allFib(4)

"""So here we have a time complexity of O(N) for the first function.
And we know that O(branches^depth) for the recursive calls. That will
give us a complexity of O(N) + O(2^depth)."""