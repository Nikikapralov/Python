path = r''


def get_the_count(line):
    to_count = ["-", ",", ".", "!", "?", "'", ':', ';']
    letters = 0
    marks = 0
    for item in line:
        if item.isalpha():
            letters += 1
        elif item in to_count:
            marks += 1
    return letters, marks


def write_to_file(to_write):
    path = r''
    with open(path, 'a') as file_output:
        file_output.write(to_write)


with open(path, 'r') as file:
    for index, line in enumerate(file):
        (letters, marks) = get_the_count(line)
        to_write = f'Line {index}: {line} ({letters})({marks})\n'
        write_to_file(to_write)


