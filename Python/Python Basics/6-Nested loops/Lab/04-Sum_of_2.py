import sys
beginning = int(input())
end = int(input())
magical_number = int(input())
sum = 0
combination = 0
for i in range(beginning, end + 1):
    for n in range (beginning, end + 1):
        combination += 1
        sum = i + n
        if sum == magical_number:
            print(f'Combination N:{combination} ({i} + {n} = {magical_number})')
            sys.exit()
if sum != magical_number:
    print(f'{combination} combinations - neither equals {magical_number}')



