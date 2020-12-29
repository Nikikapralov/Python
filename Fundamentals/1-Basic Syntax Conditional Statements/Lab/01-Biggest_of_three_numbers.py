import sys
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
highest_number = -sys.maxsize
if number_1 > highest_number:
    highest_number = number_1
if number_2 > highest_number:
    highest_number = number_2
if number_3 > highest_number:
    highest_number = number_3
print(highest_number)