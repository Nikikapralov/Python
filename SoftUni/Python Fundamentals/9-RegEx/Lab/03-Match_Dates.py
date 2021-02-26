import re
data = input()
pattern = r'\b(?P<day>\d{2})(?P<separator>[-./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})'
result = re.finditer(pattern, data)
for objekt in result:
    dictionary = objekt.groupdict()
    print(f"Day: {dictionary['day']}, Month: {dictionary['month']}, Year: {dictionary['year']}")
