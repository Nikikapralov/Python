from collections import deque


def list_manipulator(numbers, *args):
    command_1 = args[0]
    command_2 = args[1]
    other_numbers = list(args[2:])
    if command_1 == 'add':
        if command_2 == 'beginning':
            other_numbers.extend(numbers)
            return other_numbers

        elif command_2 == 'end':
            numbers.extend(other_numbers)
            return numbers
    elif command_1 == 'remove':
        if command_2 == 'beginning':
            numbers = deque(numbers)
            if other_numbers:
                [numbers.popleft() for _ in range(*other_numbers)]
                return list(numbers)
            else:
                numbers.popleft()
                return list(numbers)
        elif command_2 == 'end':
            if other_numbers:
                [numbers.pop() for _ in range(*other_numbers)]
                return numbers
            else:
                numbers.pop()
                return numbers


print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
