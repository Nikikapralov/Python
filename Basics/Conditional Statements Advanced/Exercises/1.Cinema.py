type_projection = input()
roles = int(input())
coloumns = int(input())
number_of_seats = roles * coloumns
price = 0
if type_projection == 'Premiere':
    price = number_of_seats * 12
    print(f'{price:.2f} leva')

elif type_projection == 'Normal':
    price = number_of_seats * 7.5
    print(f'{price:.2f} leva')

elif type_projection == 'Discount':
    price = number_of_seats * 5
    print(f'{price:.2f} leva')