number = int(input())
current = 0
flag = True
for row in range(1, number + 1):
    for amount_of_numbers_to_print in range(1, row + 1):
        current += 1
        print(current, end=" ")
        if current == number:
            flag = False
            break
    if not flag:
        break
    print()