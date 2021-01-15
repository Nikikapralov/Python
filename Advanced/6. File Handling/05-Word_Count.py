import re
path_words = r''
path_text = r''
path_new = r''

with open(path_words, 'r') as words_file:
    words = words_file.read().split()
words_dict = {}
for word in words:
    word = word.lower()
    if word not in words_dict:
        words_dict[word] = 0
    with open(path_text, 'r') as text_file:
        for line in text_file:
            pattern = r'\b' + word + r'((?=\s)|\W)'
            result = re.finditer(pattern, line, flags=re.IGNORECASE)
            amount = 0
            for item in result:
                amount += 1
            words_dict[word] += amount
with open(path_new, 'w') as new_file:
    for key, value in sorted(words_dict.items(), key=lambda x: -x[1]):
        new_file.write(f'{key} - {value}\n')

