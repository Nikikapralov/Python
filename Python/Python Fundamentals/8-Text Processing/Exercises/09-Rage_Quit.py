string = input()
strings = []
string_1 = []
symbols = []
numbers = []
current_string = ''
current_number = ''
result = ''
for letter in string:
    if not letter.isdigit():
        if current_number != '':
            numbers.append(current_number)
            current_number = ''
        current_string += letter.upper()
    elif letter.isdigit():
        if current_string != '':
            strings.append(current_string)
            current_string = ''
        current_number += letter

numbers.append(current_number)

for index, key in enumerate(strings):
    value = int(numbers[index])
    result += key * value
    if value != 0:
        string_1.append(key)


for iten in ''.join(string_1):
    if iten not in symbols:
        symbols.append(iten)

print(f'Unique symbols used: {len(symbols)}')
print(result)