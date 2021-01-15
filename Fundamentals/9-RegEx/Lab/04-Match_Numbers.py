import re
data = input()
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?((?=\s)|$)'
result = re.finditer(pattern, data)
list_result = [item.group() for item in result]
print(*list_result)