from collections import deque
food = int(input())
queue = deque(int(order) for order in input().split())
print(max(queue))
while queue:
    current_order = queue[0]
    if food >= current_order:
        food -= current_order
        queue.popleft()
    else:
        break

if not queue:
    print(f'Orders complete')
else:
    print('Orders left:', end=' ')
    for item in queue:
        print(item, end=' ')
