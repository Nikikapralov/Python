import re
data = input()
list_of_all_dicts = []
pattern = r'(?P<either>\||#)(?P<name>[a-zA-Z\s]+)(?P=either)(?P<date>[\d]{2}/[\d]{2}/[\d]{2})(?P=either)(?P<calories>\d+)(?P=either)'
total_calories = 0
result = re.finditer(pattern, data)
for item in result:
    dictionary = item.groupdict()
    list_of_all_dicts.append(dictionary)
    calories = int(dictionary['calories'])
    total_calories += calories

days_i_can_survive = total_calories // 2000
print(f'You have food to last you for: {days_i_can_survive} days!')
for item in list_of_all_dicts:
    print(f"Item: {item['name']}, Best before: {item['date']}, Nutrition: {item['calories']}")