import re
pattern = r'www\.[a-zA-Z0-9-]+(\.[a-z]+)+'
while True:
    data = input()
    if data:
        result = re.finditer(pattern, data)
        for item in result:
            print(item.group())
    else:
        break