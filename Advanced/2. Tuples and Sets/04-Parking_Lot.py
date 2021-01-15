parking_lot = set()
cars = int(input())
for _ in range(cars):
    direction, plate = input().split(', ')
    if direction == 'IN':
        parking_lot.add(plate)
    elif direction == 'OUT':
        parking_lot.remove(plate)
if parking_lot:
    [print(plate) for plate in parking_lot]
else:
    print('Parking Lot is Empty')