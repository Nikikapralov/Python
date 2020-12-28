result = int(input())
counter = 0
#x1 + x2 + x3 = result
for i in range(0,result + 1):
    for n in range (0, result + 1):
        for m in range (0, result + 1):
            if (i + n) + m == result:
                print(f'{i} + {n} + {m} = {result}')
                counter += 1
                print(counter)