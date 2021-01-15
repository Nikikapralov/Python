import re
data = input()
emojis = []
cool_emojis = []
pattern = r'(::|\*\*)([A-Z][a-z]{2,})(\1)'
threshold = 1

for item in data:
    if item.isdigit():
        threshold *= int(item)
result = re.finditer(pattern, data)

for item in result:
    emojis.append(item.group())

for emoji in emojis:
    coolness = 0
    for char in emoji:
        if char.isalpha():
            coolness += ord(char)
    if coolness > threshold:
        cool_emojis.append(emoji)

print(f'Cool threshold: {threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
[print(cool_emoji) for cool_emoji in cool_emojis]