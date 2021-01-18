length = int(input())
array = [1]


def tribonacci(length, array):
    if len(array) == length:
        return array
    else:
        try:
            array.append(sum([array[-1], array[-2], array[-3]]))
        except IndexError:
            array.append(sum(array))
        array = tribonacci(length, array)
        return array

array = tribonacci(length, array)
print(*array)

