string = input()
result = ''
explosion = 0
for index, char in enumerate(string):
    if char == '>':
        result += char
        explosion += int(string[index + 1])
    elif explosion != 0:
        explosion -= 1
        continue
    else:
        result += char

print(result)
