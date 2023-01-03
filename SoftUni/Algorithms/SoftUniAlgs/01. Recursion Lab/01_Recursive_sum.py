input = list(map(lambda x: int(x), "1 2 3 4".split(" ")))


def recursive_sum(input, index=0):
    if index == len(input) - 1:
        return input[index]

    return input[index] + recursive_sum(input, index + 1)


print(recursive_sum(input))
