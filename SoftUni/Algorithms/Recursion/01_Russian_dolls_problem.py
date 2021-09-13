def find_smallest_doll(size):
    if size == 1:
        return "Found smallest"
    result = find_smallest_doll(size - 1)
    return result

print(find_smallest_doll(10))