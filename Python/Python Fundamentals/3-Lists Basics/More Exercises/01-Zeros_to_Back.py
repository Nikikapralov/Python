data = input().split(', ')
result = []
amount_zeros = 0
data = [int(item) for item in data]
for index, item in enumerate(data):
    if item != 0:
        result.append(item)
    elif item == 0:
        amount_zeros += 1
for _ in range(amount_zeros):
    result.append(0)

print(result)