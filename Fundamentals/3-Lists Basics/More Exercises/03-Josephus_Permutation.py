from collections import deque


def get_input():
    numbers = deque(input().split())
    counts = int(input())
    return numbers, counts


def get_result(numbers, counts):
    result = []
    while numbers:
        for _ in range(counts - 1):
            numbers.append(numbers.popleft())
        result.append((numbers.popleft()))
    return result


numbers, counts = get_input()
result = get_result(numbers, counts)
print(f'[{",".join(result)}]')