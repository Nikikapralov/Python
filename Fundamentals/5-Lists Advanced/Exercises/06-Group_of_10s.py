import math


def group_of_ns(upper_bracket):
    list_of_items = []
    lower_bracket = upper_bracket - 10
    for item in int_numbers:
        if lower_bracket < item <= upper_bracket:
            list_of_items.append(item)
    print(f"Group of {upper_bracket}'s: {list_of_items}")


upper_bracket = 0
numbers = input().split(', ')
int_numbers = [int(number) for number in numbers]
int_numbers_copy = int_numbers.copy()
int_numbers_copy.sort(reverse=True)
biggest = int_numbers_copy[0]
largest_group = biggest / 10
if largest_group < 1:
    largest_group = 1
elif largest_group % int(largest_group) != 0:
    largest_group += 1
    largest_group = math.floor(largest_group)
largest_group *= 10
for_iterations = int(largest_group // 10)
for x in range(1, for_iterations + 1):
    upper_bracket += 10
    group_of_ns(upper_bracket)