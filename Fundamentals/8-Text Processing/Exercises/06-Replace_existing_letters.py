text = input()
clear_text = ''
last_char = -1
is_first = True
for char in text:
    if is_first:
        if text[0] == char:
            last_char = 0
            clear_text += char
            is_first = False
            continue
    else:
        if text[last_char] == char:
            last_char += 1

        else:
            clear_text += char
            last_char += 1
print(clear_text)