lines = int(input())
list_of_all_ints = []
list_result = []
for i in range(lines):
    integer = int(input())
    list_of_all_ints.append(integer)
command = input()

if command == 'even':
    for i in list_of_all_ints:
        if i % 2 == 0:
            list_result.append(i)
elif command == 'odd':
    for i in list_of_all_ints:
        if i % 2 != 0:
            list_result.append(i)
elif command == 'negative':
    for i in list_of_all_ints:
        if i < 0:
            list_result.append(i)
elif command == 'positive':
    for i in list_of_all_ints:
        if i >= 0:
            list_result.append(i)
print(list_result)