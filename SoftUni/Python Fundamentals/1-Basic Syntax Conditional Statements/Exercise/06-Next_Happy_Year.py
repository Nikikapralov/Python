year = int(input())  # 1923
current_value = ''
while True:
    Flag = False
    year += 1
    str_year = str(year)
    for index, value in enumerate(str_year):
        if Flag:
            break
        for index1, value1 in enumerate(str_year):
            if index == index1:
                continue
            if value == value1:
                Flag = True
                break
    if Flag:
        continue
    else:
        break
print(year)
