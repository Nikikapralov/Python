number_of_people = int(input())
people_who_fit = int(input())
course = 0
while True:
    course += 1
    number_of_people -= people_who_fit
    if number_of_people <= 0:
        break
print(course)