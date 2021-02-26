data = input().split(', ')
if data[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
    exit()
for index, animal in enumerate(data):
    if animal == 'wolf':
        wolf_index = int(index)
        sheep_index_plus_1 = wolf_index + 1
        sheep_number = len(data) - sheep_index_plus_1
        break
print(f'Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!')
