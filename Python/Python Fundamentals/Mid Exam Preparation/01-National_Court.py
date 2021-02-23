employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
total_people_count = int(input())
hour = 0
while True:
    if hour % 4 == 0 and hour != 0:
        hour += 1
        continue
    if total_people_count <= 0:
        break
    total_people_count -= (employee_1 + employee_2 + employee_3)
    hour += 1
print(f'Time needed: {hour}h.')
