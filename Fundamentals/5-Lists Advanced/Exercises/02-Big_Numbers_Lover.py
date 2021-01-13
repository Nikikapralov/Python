numbers = input().split()
numbers.sort(reverse=True)
strings = [int(numbers[x]) for x in range(len(numbers))]
strings.sort(reverse=True)
for y in range(len(numbers)):
    print(numbers[y], end='')
print('')
for z in range(len(strings)):
    print(strings[z], end='')
