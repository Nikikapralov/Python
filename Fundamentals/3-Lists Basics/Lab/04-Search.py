number_of_lines = int(input())
word = input()
list_1 = []
list_2 = []
for n in range(number_of_lines):
    string = input()
    list_1.append(string)
print(list_1)

for index, value in enumerate(list_1):
    if word in value:
        list_2.append(value)

print(list_2)
