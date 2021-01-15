array = [int(number) for number in input().split()]
total = 0
biggest_5 = []
amount = len(array)
for x in array:
    total += x
average_value = total / amount
for item in array:
    if item > average_value:
        biggest_5.append(item)
biggest_5.sort(reverse=True)
while len(biggest_5) > 5:
    biggest_5.pop(-1)
str_biggest_5 = [str(y) for y in biggest_5]
output = ' '.join(str_biggest_5)
if len(biggest_5) == 0:
    print('No')
else:
    print(output)
