lines = int(input())
positive_ints = []
negative_ints = []
count_of_positive_ints = 0
sum_of_negative_ints = 0
for x in range (lines):
    integer = int(input())
    if integer >= 0:
        positive_ints.append(integer)
        count_of_positive_ints += 1
    else:
        negative_ints.append(integer)
        sum_of_negative_ints += integer
print(positive_ints)
print(negative_ints)
print(f'Count of positives: {count_of_positive_ints}. Sum of negatives: {sum_of_negative_ints}')
