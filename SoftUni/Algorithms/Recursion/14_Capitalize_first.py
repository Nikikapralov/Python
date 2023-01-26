def cap_first(array, index=0):
    if index == len(array):
        return array

    array[index] = array[index].capitalize()
    return cap_first(array, index + 1)


print(cap_first(['car', 'taco', 'banana']))