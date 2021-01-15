import re
data = input()
pattern = r'\b(^|(?<=\s))(?P<user>[a-zA-Z0-9]+(([-._][a-zA-Z0-9]+)+)?)@[a-zA-Z]+(([-][a-zA-Z]+)?)+(\.[a-zA-Z]+(([-][a-zA-Z]+)?)+)+($|(?![\w@#$%^&*-]))'
result = re.finditer(pattern, data)
for item in result:
    print(item.group())