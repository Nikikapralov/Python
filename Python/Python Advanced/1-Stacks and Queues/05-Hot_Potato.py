from collections import deque
kids = deque(name for name in input().split())
tosses = int(input())


def hot_potato(kids, target):
    counter = 1
    while counter != target:
        current_kid = kids.popleft()
        kids.append(current_kid)
        counter += 1
    loser = kids.popleft()
    print(f'Removed {loser}')
    return


while len(kids) > 1:
    hot_potato(kids, tosses)
winner = kids[0]
print(f'Last is {winner}')
