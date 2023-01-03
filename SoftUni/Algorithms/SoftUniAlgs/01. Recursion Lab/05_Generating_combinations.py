input = [1, 2, 3, 4]
combo = [0, 0]


def generate_combinations(input, index, index_input, combo=[0, 0]):
    if index == len(combo):
        print(" ".join([str(x) for x in combo]))
        return

    for i in range(index_input, len(input)):
        combo[index] = input[i]
        generate_combinations(input, index + 1, i + 1, combo)


generate_combinations(input, 0, 0)