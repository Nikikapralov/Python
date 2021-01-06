import sys
numbers = input().split()
int_numbers = [int(x) for x in numbers]
n = int(input())
big_numbers = []
for x in range(n):
    smallest = sys.maxsize
    index1 = 0
    for index, value in enumerate(int_numbers):
        if value < smallest:
            smallest = value
            index1 = index
        else:
            continue
    int_numbers.pop(index1)
print(int_numbers)
