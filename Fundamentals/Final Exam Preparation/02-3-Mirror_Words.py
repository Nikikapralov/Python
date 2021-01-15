import re
data = input()
pattern = r'(?P<surround>@|#)(?P<word_one>[a-zA-Z][a-zA-Z][a-zA-Z]+)(?P=surround)(?P=surround)(?P<word_two>[a-zA-Z][a-zA-Z][a-zA-Z]+)(?P=surround)'
result = re.finditer(pattern, data)
mirror_words = []
matching_words_counter = 0
matching_words = False
mirror_words_is = False
for item in result:
    word_one = item.group('word_one')
    word_two = item.group('word_two')
    word_two_reversed = word_two[::-1]
    matching_words = True
    matching_words_counter += 1
    if word_one == word_two_reversed:
        mirror_words.append(f'{word_one} <=> {word_two}')
        mirror_words_is = True
if not matching_words:
    print('No word pairs found!')
elif matching_words:
    print(f'{matching_words_counter} word pairs found!')
if not mirror_words_is:
    print('No mirror words!')
elif mirror_words_is:
    print('The mirror words are:')
    print(f'{", ".join(mirror_words)}')
