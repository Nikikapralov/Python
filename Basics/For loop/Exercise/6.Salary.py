amount_of_tabs = int(input())
salary = int(input())
tax = 0

for i in range(amount_of_tabs):
    name_of_website = input()
    if name_of_website == 'Facebook':
        tax += 150
    elif name_of_website == 'Instagram':
        tax += 100
    elif name_of_website == 'Reddit':
        tax += 50
    if tax >= salary:
        print('You have lost your salary.')
        break

if tax < salary:
    print(f'{salary - tax:.0f}')
