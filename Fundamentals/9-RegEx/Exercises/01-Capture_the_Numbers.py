import re
pattern = r'\d+'
list_result = []
while True:
    data = input()
    if data:
        result = re.findall(pattern, data)
        for item in result:
            if item.isdigit():
                list_result.append(item)
    else:
        break

print(*list_result)
