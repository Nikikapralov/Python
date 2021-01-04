number = int(input())
for n in range(2, number):
    if number % n == 0:
        print('False')
        exit()
    else:
        continue
print('True')
