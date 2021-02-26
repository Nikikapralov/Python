def ascii(char_1, char_2):
    number_1 = int(ord(char_1))
    number_2 = int(ord(char_2))
    for number in range(number_1 + 1, number_2):
        char = chr(number)
        print(char, end=' ')
    return


char_1 = input()
char_2 = input()
start = ascii(char_1=char_1, char_2=char_2)

