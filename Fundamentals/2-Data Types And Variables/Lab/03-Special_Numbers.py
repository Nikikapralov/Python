number = int(input())
for n in range(1, number + 1):
    str_n = str(n)
    special_number = 0
    for index, value in enumerate(str_n):
        value = int(value)
        special_number += value
    if special_number == 5 or special_number == 7 or special_number == 11:
        print(f'{n} -> True')
    else:
        print(f'{n} -> False')

#Zadachata moje da se reshi i s (for char in (str_n)) kato iteratevame prez vseki char na chisloto i posle gi subirame v otdelna promenliva kakto gore sum go reshil.



