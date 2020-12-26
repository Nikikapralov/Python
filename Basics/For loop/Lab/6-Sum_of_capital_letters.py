text = input()
sum = 0
for character in text:
    if character == 'a':
        sum += 1
    elif character == 'e':
        sum += 2
    elif character == 'i':
        sum += 3
    elif character == 'o':
        sum += 4
    elif character == 'u':
        sum += 5
print(sum)