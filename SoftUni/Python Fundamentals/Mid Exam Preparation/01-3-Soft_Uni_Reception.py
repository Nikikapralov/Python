employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
efficiency = employee_3 + employee_2 + employee_1
students_count = int(input())
hour = 0
while True:
    if students_count == 0:
        break
    hour += 1
    if hour % 4 == 0:
        continue
    students_count -= efficiency
    if students_count <= 0:
        break

print(f'Time needed: {hour}h.')


