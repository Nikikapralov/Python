factor = int(input())
count = int(input())
list_of_numbers = [factor]
number = factor
while count > len(list_of_numbers):
    number += factor
    list_of_numbers.append(number)
list_of_numbers.sort()
print(list_of_numbers)