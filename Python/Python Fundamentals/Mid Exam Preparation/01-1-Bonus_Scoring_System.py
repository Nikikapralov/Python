import math
count_of_students = int(input())
amount_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendance = 0
for student in range(count_of_students):
    attendances = int(input())
    bonus = attendances / amount_of_lectures * (5 + additional_bonus)
    if bonus >= max_bonus:
        max_bonus = bonus
        max_attendance = attendances
print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {max_attendance} lectures.')

