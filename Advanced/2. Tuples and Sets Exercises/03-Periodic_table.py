lines = int(input())
elements = set()
for _ in range(lines):
    data = input().split()
    [elements.add(element) for element in data]
[print(element) for element in elements]
