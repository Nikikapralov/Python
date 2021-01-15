equation = input()
stack_opening = []
all_equations = []
for index, item in enumerate(equation):
    if item == '(':
        stack_opening.append(index)

    elif item == ')':
        open_index = stack_opening.pop()
        close_index = index
        current_equation = equation[open_index:close_index + 1]
        all_equations.append(current_equation)

for item in all_equations:
    print(item)
