lines = int(input())
unique_names = set()
[unique_names.add(input()) for _ in range(lines)]
[print(name) for name in unique_names]
