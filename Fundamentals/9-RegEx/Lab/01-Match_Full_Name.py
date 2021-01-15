import re
data = input()
pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
result = re.findall(pattern, data)
print(' '.join(result))