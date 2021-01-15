import collections
queue = collections.deque()
name = input()
while name != 'End':
    if name == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(name)
    name = input()

print(f'{len(queue)} people remaining.')
