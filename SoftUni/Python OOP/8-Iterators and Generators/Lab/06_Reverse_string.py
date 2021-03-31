def reverse_text(string):
    current_index = 0
    while True:
        current_index -= 1
        try:
            yield string[current_index]
        except IndexError:
            break

for char in reverse_text("step"):
    print(char, end='')
