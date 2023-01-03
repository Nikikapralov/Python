input = 3
slots = [0 for _ in range(input)]


def generate_vectors(slots, combos=2, index=0):
    if index == len(slots):
        print("".join([str(x) for x in slots]))
        return

    for entry in range(combos):
        slots[index] = entry
        generate_vectors(slots, combos, index + 1)


generate_vectors(slots, combos=3)
