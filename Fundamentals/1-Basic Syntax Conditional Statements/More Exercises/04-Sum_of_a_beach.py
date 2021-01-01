import re
data = input().lower()
pattern = r'water|sun|sand|fish'
result = re.findall(pattern, data)
print(len(result))
