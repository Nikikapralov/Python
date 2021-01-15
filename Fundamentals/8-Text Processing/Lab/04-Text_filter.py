class Text:
    def __init__(self, data):
        self.data = data


class BannedWord:
    def __init__(self, word):
        self.word = word
        self.length = len(self.word)


def filter_text(text_data, banned_word_data):
    text_1.data = text_data.replace(banned_word_data, '*' * banned_word.length)
    result = text_1.data
    return result


list_of_words = input().split(', ')
text_1 = Text(input())
final = ''

for item in list_of_words:
    banned_word = BannedWord(item)
    final = filter_text(text_1.data, banned_word.word)

print(final)

