intellect = int(input())
power = int(input())
sex = input()

if sex == 'female':
    if intellect >= 80 and power >= 80:
        print('Queen Bee')
    elif intellect >= 80:
        print('Repairing Bee')
    elif intellect >= 60:
        print('Cleaning Bee')
    elif power >= 60:
        print('Guard Bee')
    else:
        print('Worker Bee')

elif sex == 'male':
    if intellect >= 80:
        print('Repairing Bee')
    elif intellect >= 60:
         print('Cleaning Bee')
    elif power >= 80:
         print('Drone Bee')
    elif power >= 60:
        print('Guard Bee')
    else:
        print('Worker Bee')
