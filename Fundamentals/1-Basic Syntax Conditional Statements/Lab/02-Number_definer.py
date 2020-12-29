number = float(input())
NUMBER_X = 0
NUMBER_X_SPELLED = 'zero'
abs_number = abs(number)
if number == NUMBER_X:
    print(NUMBER_X_SPELLED)
elif abs_number < 1:
    print('small', end=' ')
elif abs_number > 1000000:
    print('large', end=' ')
if number > 0:
    print('positive')
elif number < 0:
    print('negative')