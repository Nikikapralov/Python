day_of_the_week = str(input())

if day_of_the_week == str('Monday') or day_of_the_week == str('Tuesday') or day_of_the_week == str('Wednesday') or day_of_the_week == str('Thursday') or day_of_the_week == str('Friday'):
    print('Working day')

elif day_of_the_week == str('Saturday') or day_of_the_week == str('Sunday'):
    print('Weekend')

else:
    print('Error')
