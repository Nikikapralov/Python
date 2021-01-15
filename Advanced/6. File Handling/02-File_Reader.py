path = r''
file = open(path, 'r')
sum_of_nums = 0
while True:
    current_number = file.readline()
    if not current_number:
        break
    current_number = int(current_number)
    sum_of_nums += current_number
print(sum_of_nums)
