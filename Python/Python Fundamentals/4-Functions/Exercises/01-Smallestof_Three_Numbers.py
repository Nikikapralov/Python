import sys


def smallest_number():
    smallest = sys.maxsize
    for n in range(3):
        number = int(input())
        if number < smallest:
            smallest = number
    return smallest


execute = smallest_number()
print(execute)
