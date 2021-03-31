from itertools import permutations


def possible_permutations(my_list):
    for item in permutations(my_list):
        yield list(item)


# A Python program to print all combinations
# of given length with unsorted input.
from itertools import combinations

# Get all combinations of [2, 1, 3]
# and length 2
comb = combinations([2, 1, 3], 2)

# Print the obtained combinations
for i in list(comb):
    print(i)