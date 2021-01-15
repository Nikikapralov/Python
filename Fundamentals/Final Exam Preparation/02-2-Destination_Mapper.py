import re
travel_points = 0
pattern = r'(?P<prefix>=|/)(?P<name>[A-Z][A-Za-z][A-Za-z]+)(?P=prefix)'
data = input()
names = []
result = re.finditer(pattern, data)
for item in result:
    dictionary = item.groupdict()
    names.append(dictionary['name'])
for travel_point in names:
    travel_points += len(travel_point)
print(f'Destinations: {", ".join(names)}')
print(f'Travel Points: {travel_points}')