weekday = input()

if weekday == 'Monday' or weekday == 'Tuesday' or weekday == 'Friday':
    print('12')
elif weekday == 'Wednesday' or weekday == 'Thursday':
    print('14')
elif weekday == 'Sunday' or weekday == 'Saturday':
    print('16')