string = input()
stack_string = []
for letter in string:
    stack_string.append(letter)

reversed_string = ''
while stack_string:
    for index in range(len(stack_string) - 1, -1, -1):
        reversed_string += stack_string[index]
        stack_string.pop()

print(reversed_string)

#reversed_string += stack_string.pop()
#without for cycle
