number = int(input())
def loading_bar(number):
    if number == 0:
        print('0% [..........]')
        print('Still loading...')
    elif number == 10:
        print('10% [%.........]')
        print('Still loading...')
    elif number == 20:
        print('20% [%%........]')
        print('Still loading...')
    elif number == 30:
        print('30% [%%%.......]')
        print('Still loading...')
    elif number == 40:
        print('40% [%%%%......]')
        print('Still loading...')
    elif number == 50:
        print('50% [%%%%%.....]')
        print('Still loading...')
    elif number == 60:
        print('60% [%%%%%%....]')
        print('Still loading...')
    elif number == 70:
        print('70% [%%%%%%%...]')
        print('Still loading...')
    elif number == 80:
        print('80% [%%%%%%%%..]')
        print('Still loading...')
    elif number == 90:
        print('90% [%%%%%%%%%.]')
        print('Still loading...')
    elif number == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')

execute = loading_bar(number)