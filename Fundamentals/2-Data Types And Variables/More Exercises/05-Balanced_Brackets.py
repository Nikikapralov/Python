n_lines = int(input())
balanced = True
for _ in range(n_lines):
    data = input()
    if balanced:
        if data == '(' or data == ')':
            balanced = False
            previous_data = data
    elif not balanced:
        if previous_data == '(' and data == ')':
            balanced = True
if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

