from itertools import combinations
names = input().split(', ')
chairs = int(input())
result = combinations(names, chairs)
[print(', '.join(x)) for x in result]