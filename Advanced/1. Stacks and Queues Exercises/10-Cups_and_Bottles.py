from collections import deque
cups = deque([int(cup) for cup in input().split()])
stack_bottles = [int(bottle) for bottle in input().split()]
spilled_water = 0
result = ''
while True:
    if not cups:
        print(f'Bottles:', end='')
        for index in range(len(stack_bottles) - 1, -1, -1):
            result += ' ' + str(stack_bottles[index])
        print(result)
        break
    elif not stack_bottles:
        print(f'Cups:', end='')
        for index in range(len(cups)):
            result += ' ' + str(cups[index])
        print(result)
        break

    current_cup = cups.popleft()
    current_bottle = stack_bottles.pop()
    current_cup -= current_bottle
    if current_cup <= 0:
        spilled_water += abs(current_cup)
    else:
        cups.appendleft(current_cup)

print(f'Wasted litters of water: {spilled_water}')
