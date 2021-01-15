path = r''
to_replace = ["-", ",", ".", "!", "?"]
with open(path, 'r') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            for replacement in to_replace:
                line = line.replace(replacement, '@')
            line_reversed = ' '.join(line.split()[::-1])
            print(line_reversed)

