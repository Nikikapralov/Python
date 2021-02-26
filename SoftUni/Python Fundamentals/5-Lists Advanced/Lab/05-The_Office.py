happiness = input().split()
improvement_factor = int(input())
int_happiness = [int(integer) for integer in happiness]
are_you_happy = list(map(lambda number: number * improvement_factor, int_happiness))
average = sum(are_you_happy) / len(int_happiness)
employees_who_are_more_than_average_happy = [employee for employee in are_you_happy if employee >= average]
if len(employees_who_are_more_than_average_happy) >= len(happiness) // 2:
    print(f'Score: {len(employees_who_are_more_than_average_happy)}/{len(happiness)}. Employees are happy!')
else:
    print(f'Score: {len(employees_who_are_more_than_average_happy)}/{len(happiness)}. Employees are not happy!')
