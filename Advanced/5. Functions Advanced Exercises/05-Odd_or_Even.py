def compute(command, numbers):
    if command == 'Odd':
        sum_odd = sum(list(filter(lambda x: x % 2 == 1, numbers)))
        return sum_odd * len(numbers)
    elif command == 'Even':
        sum_even = sum(list(filter(lambda x: x % 2 == 0, numbers)))
        return sum_even * len(numbers)


command = input()
numbers = [int(x) for x in input().split()]
print(compute(command, numbers))
