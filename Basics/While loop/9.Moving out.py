width = int(input())
length = int(input())
heigth = int(input())
boxes = input()
available_space = width * length * heigth
leftover_space = available_space
while boxes != 'Done':
    boxes = int(boxes)
    leftover_space -= boxes
    if leftover_space <= 0:
        print(f'No more free space! You need {abs(leftover_space)} Cubic meters more.')
        break
    boxes = input()
if leftover_space > 0:
    print(f'{leftover_space} Cubic meters left.')
