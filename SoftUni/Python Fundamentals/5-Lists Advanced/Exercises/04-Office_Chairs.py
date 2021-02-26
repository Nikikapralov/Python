rooms = int(input())
collected_chairs = 0
Flag = False
for room_nmbr in range(1, rooms + 1):
    room = input().split()
    chairs = len(room[0])
    people = int(room[1])
    chairs_left = chairs - people
    if chairs_left < 0:
        print(f'{abs(chairs_left)} more chairs needed in room {room_nmbr}')
        Flag = True
    else:
        collected_chairs += chairs_left
if not Flag:
    print(f'Game On, {collected_chairs} free chairs left')
