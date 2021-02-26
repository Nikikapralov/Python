numbers = input()
normal_list = numbers.split()
inverted_list = []
for i in normal_list:
    i = int(i)
    if i < 0:
        inverted_list.append((abs(i)))
    elif i >= 0:
        inverted_list.append(-i)
print(inverted_list)
