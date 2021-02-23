total_sold_tickets = 0
counter1 = 0
student = 0
kid = 0
standard = 0
percentage_full = 0
percentage_student = 0
percentage_standard = 0
percentage_kid = 0
while True:
    name = input()
    if name == 'Finish':
        break
    free_spots = int(input())
    counter1 = 0
    while True:
        kind_of_ticket = input()
        if kind_of_ticket != 'End':
            counter1 += 1
            total_sold_tickets += 1
        if kind_of_ticket == 'student':
            student += 1
        elif kind_of_ticket == 'kid':
            kid += 1
        elif kind_of_ticket == 'standard':
            standard += 1
        percentage_full = counter1 / free_spots * 100
        if counter1 == free_spots or kind_of_ticket == "End":
            print(f'{name} - {percentage_full:.2f}% full.')
            break
percentage_student = student / total_sold_tickets * 100
percentage_standard = standard / total_sold_tickets * 100
percentage_kid = kid / total_sold_tickets * 100
print(f'Total tickets: {total_sold_tickets}')
print(f'{percentage_student:.2f}% student tickets.')
print(f'{percentage_standard:.2f}% standard tickets.')
print(f'{percentage_kid:.2f}% kids tickets.')


