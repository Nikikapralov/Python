maximum_amount_of_bad_grades = int(input())
amount_of_bad_grades = 0
number_of_problems = 0
average_score = 0
total_grades = 0
grade = 0
last_problem = 0
while True:
    name_of_task = input()
    if name_of_task != 'Enough':
        last_problem = name_of_task
    if name_of_task == 'Enough':
        print(f'Average score: {average_score:.2f}')
        print(f'Number of problems: {number_of_problems}')
        print(f'Last problem: {last_problem}')
        break
    grade = int(input())
    number_of_problems += 1
    total_grades += grade
    average_score = total_grades / number_of_problems
    if grade <= 4:
        amount_of_bad_grades += 1
    if amount_of_bad_grades == maximum_amount_of_bad_grades:
        print(f'You need a break, {amount_of_bad_grades} poor grades.')
        break

