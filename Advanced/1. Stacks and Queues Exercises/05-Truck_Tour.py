from collections import deque
amount_trucks = int(input())
trucks = deque()
for _ in range(amount_trucks):
    trucks.append([int(item) for item in input().split()])

for x in range(amount_trucks):
    petrol = 0
    is_valid = True
    for _ in range(amount_trucks):
        current_truck = trucks.popleft()
        petrol += current_truck[0]
        distance = current_truck[1]
        petrol -= distance
        if petrol < 0:
            is_valid = False
        trucks.append(current_truck)

    if is_valid:
        print(x)
        break

    trucks.append(trucks.popleft())
