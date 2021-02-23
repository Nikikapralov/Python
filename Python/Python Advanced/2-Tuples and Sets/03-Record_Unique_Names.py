n = int(input())
names = []
for i in range(n):
    name = input()
    names.append(name)
set_names = set(names)
for item in set_names:
    print(item)
