stack_clothes = [int(item) for item in input().split()]
capacity = int(input())
racks = 0
place_taken = 0
first = True
while stack_clothes:
    item_space = stack_clothes.pop()
    place_taken += item_space
    if place_taken < capacity:
        if first:
            racks += 1
            first = False
        continue
    elif place_taken == capacity:
        place_taken = 0
        first = True
    elif place_taken > capacity:
        racks += 1
        place_taken = 0
        place_taken += item_space
        first = False

print(racks)
