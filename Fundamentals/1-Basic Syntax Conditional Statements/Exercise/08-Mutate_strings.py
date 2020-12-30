string1 = input()  # Kitty
string2 = input()  # Doggy
list1 = list(string1)
list2 = list(string2)
Flag = False
old_list = 0
new_list = 0
for index, value in enumerate(string1):
    if Flag:
        break
    for index1, value1 in enumerate(string2):
        if list1 == list2:
            Flag = True
            break
        if (index == index1) and (value != value1):
            list1[index1] = list2[index1]
            for x in range(len(list1)):
                print(list1[x], end='')
            print()

