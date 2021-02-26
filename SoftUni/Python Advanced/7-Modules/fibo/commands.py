def create(number):
    if number == 0:
        return []
    if number == 1:
        return [0]
    numbers = [0, 1]
    while len(numbers) < number:
        new_number = numbers[-1] + numbers[-2]
        numbers.append(new_number)
    return numbers


def locate(to_locate, sequence):
    try:
        answer = sequence.index(to_locate)
    except ValueError:
        return None
    return answer
