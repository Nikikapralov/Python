import re
pattern = r'\b(?P<underscore>_)(?P<variable>[a-zA-Z0-9]+)\b'
list_result = []
data = input()
result = re.finditer(pattern, data)
for item in result:
    dictionary = item.groupdict()
    list_result.append(dictionary['variable'])
print(*list_result, sep=',')
