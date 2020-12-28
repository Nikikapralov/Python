number_of_the_jury_people = int(input())
amount_of_presentations = 0
biggest_grade = 0
biggest_middle_grade = 0
while True:
    presentation_name = input()
    if presentation_name == 'Finish':
        break
    amount_of_presentations += 1
    total_grade = 0
    middle_grade = 0
    for i in range(number_of_the_jury_people):
        grade = float(input())
        total_grade += grade
    middle_grade = total_grade / number_of_the_jury_people
    biggest_grade += middle_grade
    biggest_middle_grade = biggest_grade / amount_of_presentations
    print(f'{presentation_name} - {middle_grade:.2f}.')
print(f"Student's final assessment is {biggest_middle_grade:.2f}.")