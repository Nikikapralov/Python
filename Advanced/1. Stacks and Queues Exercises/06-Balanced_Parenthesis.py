stack_parenthesis = []
expression = input()
for current in expression:
    if current == '{' or current == '[' or current == '(':
        stack_parenthesis.append(current)

    if stack_parenthesis:
        if current == '}' and stack_parenthesis[-1] == '{':
            stack_parenthesis.pop()
        elif current == ']' and stack_parenthesis[-1] == '[':
            stack_parenthesis.pop()
        elif current == ')' and stack_parenthesis[-1] == '(':
            stack_parenthesis.pop()
    else:
        print('NO')
        exit()
if not stack_parenthesis:
    print('YES')
else:
    print('NO')