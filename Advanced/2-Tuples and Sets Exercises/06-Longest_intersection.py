lines = int(input())
all_intersections = []
for _ in range(lines):
    sets = []
    data = input().split('-')
    for item in data:
        start, end = item.split(',')
        current_set = set([int(x) for x in range(int(start), int(end) + 1)])
        sets.append(current_set)
    intersection = sorted(sets[0].intersection(sets[1]))
    all_intersections.append(intersection)
longest_intersection = sorted(all_intersections, key=len, reverse=True)[0]
print(f'Longest intersection is {longest_intersection} with length {len(longest_intersection)}')
