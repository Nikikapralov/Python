number_n = int(input())
number_l = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
Flag = False
real_symbol_5 = 0
while True:
    if Flag:
        break
    for symbol_1 in range(1, number_n + 1):
        if symbol_1 == (number_n):
            Flag = True
            break
        for symbol_2 in range(1, number_n + 1):
            for index, symbol_3 in enumerate(alphabet):
                if index == number_l:
                    break
                for index2, symbol_4 in enumerate(alphabet):
                    if index2 == number_l:
                        break
                    for symbol_5 in range(1, number_n + 1):
                        if symbol_5 == (number_n + 1):
                            break
                        if symbol_5 > symbol_1 and symbol_5 > symbol_2:
                            real_symbol_5 = symbol_5
                        else:
                            continue
                        symbol_1 = str(symbol_1)
                        symbol_2 = str(symbol_2)
                        real_symbol_5 = str(real_symbol_5)
                        print(symbol_1 + symbol_2 + symbol_3 + symbol_4 + real_symbol_5, end=' ')
                        symbol_2 = int(symbol_2)
                        symbol_1 = int(symbol_1)
