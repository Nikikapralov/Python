import sys
name = input()
current_grade = 0
fails = 0
average_grade = 0
grade_sum = 0
while True:
    grade = float(input())
    if grade >= 4:
        current_grade += 1
        grade_sum += grade
    elif grade < 4:
        fails += 1

    if fails > 1:
        print(f'{name} has been excluded at {current_grade + 1} grade')
        sys.exit()
    if current_grade == 12:
        average_grade = grade_sum / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break

