import math
income = float(input())
grades = float(input())
minimum_wage = float(input())
is_social_scholarship = income < minimum_wage and grades > 4.5
social_scholarship = minimum_wage * 0.35
excellent_grades_scholarship = grades * 25

if is_social_scholarship and grades >=5.5:
    if social_scholarship > excellent_grades_scholarship:
        print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
    elif social_scholarship < excellent_grades_scholarship:
        print(f'You get a scholarship for excellent results {math.floor(excellent_grades_scholarship)} BGN')
    else:
        print(f'You get a scholarship for excellent results {math.floor(excellent_grades_scholarship)} BGN')

elif income < minimum_wage and grades > 4.5:
    print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')


elif grades >= 5.5:
    print(f'You get a scholarship for excellent results {math.floor(excellent_grades_scholarship)} BGN')

else:
    print('You cannot get a scholarship!')