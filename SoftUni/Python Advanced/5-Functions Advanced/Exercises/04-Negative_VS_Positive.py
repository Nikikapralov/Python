def separate(numbers):
    negative = list(filter(lambda x: x < 0, numbers))
    positive = list(filter(lambda x: x > 0, numbers))
    return negative, positive


negative, positive = separate([int(x) for x in input().split()])
sum_negative = sum(negative)
sum_poisitve = sum(positive)
print(sum_negative)
print(sum_poisitve)
if abs(sum_negative) > sum_poisitve:
    print(f'The negatives are stronger than the positives')
elif abs(sum_negative) < sum_poisitve:
    print(f'The positives are stronger than the negatives')