numbers_list = []
for n in range(3):
    number = int(input())
    numbers_list.append(number)
result = sorted(numbers_list, reverse=True)
print(result[0])