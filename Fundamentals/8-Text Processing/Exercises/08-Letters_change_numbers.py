strings_list = input().split()
numbers = [x for x in range(1, 27)]
upper_alphabet = {}
lower_alphabet = {}
sums = []
n = 1
for x in range(65, 91):
    for number in numbers:
        if number == x - (x-n):
            upper_alphabet[chr(x)] = number
            n += 1
            break
n = 1
for x in range(97, 123):
    for number in numbers:
        if number == x - (x-n):
            lower_alphabet[chr(x)] = number
            n += 1
            break


def upper(letter, number, is_after, sum_2):
    position = int(upper_alphabet[letter])
    if not is_after:
        sum_2 = number / position
        return sum_2
    else:
        sum_2 = - position
        return sum_2


def lower(letter, number, is_after, sum_2):
    position = int(lower_alphabet[letter])
    if not is_after:
        sum_2 = number * position
        return sum_2
    else:
        sum_2 = position
        return sum_2



for string in strings_list:
    number = ''
    sum_1 = 0
    is_after = False
    done = False
    for letter in string:
        if not done:
            for letter_1 in string:
                if letter_1.isdigit():
                    number += letter_1
                    done = True
        if letter.isupper():
            sum_1 += upper(letter, int(number), is_after, sum_1)
            is_after = True
        elif letter.islower():
            sum_1 += lower(letter, int(number), is_after, sum_1)
            is_after = True
    sums.append(sum_1)


end_result = sum(sums)
print(f'{end_result:.2f}')


