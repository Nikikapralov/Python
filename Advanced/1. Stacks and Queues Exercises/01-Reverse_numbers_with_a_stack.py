numbers = [item for item in input().split()]
numbers_reversed = []
while numbers:
    numbers_reversed.append(numbers.pop())

print(*numbers_reversed)