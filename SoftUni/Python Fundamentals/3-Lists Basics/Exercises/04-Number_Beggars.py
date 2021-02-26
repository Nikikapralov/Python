numbers = input().split(', ')
int_numbers = [int(i) for i in numbers]
beggars = int(input())
beggars_take = []
for i in range(beggars):
    beggars_take.append(0)
index = len(numbers[0])
while len(numbers) > 0:
    index_numbers = 0
    beggars_take_index = 0
    for beggar in range(beggars):
        if len(numbers) == 0:
            break
        beggars_take[beggars_take_index] += int_numbers[index_numbers]
        int_numbers.pop(0)
        numbers.pop(0)
        beggars_take_index += 1
print(beggars_take)
