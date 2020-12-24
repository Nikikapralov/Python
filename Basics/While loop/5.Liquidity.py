my_input = input()
total_money = 0
while my_input != 'NoMoreMoney':
    my_input = float(my_input)
    if my_input < 0:
        print('Invalid operation!')
        break
    total_money += my_input
    print(f'Increase: {my_input:.2f}')
    my_input = input()
print(f'Total: {total_money:.2f}')
