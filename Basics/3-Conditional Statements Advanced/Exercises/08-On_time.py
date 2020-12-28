hour = int(input())
minute = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_time = hour * 60 + minute
arrival_time = hour_of_arrival * 60 + minute_of_arrival
difference = exam_time - arrival_time

mm1 = 60 - (difference % 60)
mm2 = abs(difference % 60)
hh = abs(difference) // 60

if minute == 0 and minute_of_arrival == 0:
    mm1 = 0
    mm2 = 0
#navreme
if difference >= 0 and difference <= 30:
    print('On time')
elif difference > 30:
    print('Early')
elif difference < 0:
    print('Late')


if difference > 0 and difference < 60:
    print(f'{mm2} minutes before the start')
elif difference >= 60:
    print(f'{hh}:{mm2:02d} hours before the start')

elif difference < 0 and difference > -60:
    print(f'{mm1} minutes after the start')
elif difference <= -60:
    print(f'{hh}:{mm1:02d} hours after the start')

