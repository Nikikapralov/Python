import math
leap_year_or_not = input()
holidays = int(input())
weekends_in_home_city = int(input())

if holidays >= 0 and weekends_in_home_city >= 0:
    volleyball_in_sunday = weekends_in_home_city
    volleyball_in_holidays = holidays * (2 / 3)
    volleyball_in_weekends = (48 - weekends_in_home_city) * (3 / 4)
    total_volleyball = volleyball_in_holidays + volleyball_in_sunday + volleyball_in_weekends
    if leap_year_or_not == 'normal':
        print(math.floor(total_volleyball))
    elif leap_year_or_not == 'leap':
        total_volleyball += total_volleyball * 0.15
        print(math.floor(total_volleyball))


