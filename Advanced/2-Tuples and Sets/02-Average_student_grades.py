students_grades_dict = {}
amount_students = int(input())
for n in range(amount_students):
    student, grade = input().split()
    if student not in students_grades_dict:
        students_grades_dict[student] = []
    students_grades_dict[student].append(float(grade))

for key, value in students_grades_dict.items():
    average = sum(value) / len(value)
    mark_string = " ".join(f'{grade:.2f}' for grade in value)
    print(f'{key} -> {mark_string} (avg: {average:.2f})')