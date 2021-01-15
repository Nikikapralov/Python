def combinations(string):
    out = []
    if len(string) == 1:
        return string
    else:
        for index, value in enumerate(string):
            for item in combinations(string[:index] + string[index + 1:]):
                out += [value + item]
    return out


permutations = combinations(list(input()))
[print(x) for x in permutations]
