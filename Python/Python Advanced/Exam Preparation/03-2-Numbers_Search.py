def check_for_duplicates(number, numbers):
    result = numbers.count(number)
    if result > 1:
        return True
    else:
        return False


def numbers_searching(*args):
    numbers = sorted([int(x) for x in args])
    numbers_set = sorted(set(numbers))
    highest_number = max(numbers_set)
    missing_number = None
    duplicates = set()
    for number in numbers_set:
        current_number = number
        if current_number == highest_number:
            if check_for_duplicates(current_number, numbers):
                duplicates.add(current_number)
                continue
            else:
                continue
        should_be_next_number = current_number + 1
        if should_be_next_number not in numbers:
            missing_number = should_be_next_number
        if check_for_duplicates(current_number, numbers):
            duplicates.add(current_number)
    sorted_duplicates = sorted(duplicates)

    result = [missing_number, sorted_duplicates]
    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))



