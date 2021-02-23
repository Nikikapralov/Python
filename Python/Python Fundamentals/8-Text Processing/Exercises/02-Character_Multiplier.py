string_1, string_2 = input().split()
result = 0
index = 0
if len(string_1) >= len(string_2):
    longer_string = string_1
    shorter_string = string_2
else:
    longer_string = string_2
    shorter_string = string_1

for char in shorter_string:
    result_from_multiply = ord(char) * ord(longer_string[index])
    result += result_from_multiply
    index += 1

left = longer_string[len(shorter_string):]
for item in left:
    result += ord(item)

print(result)
