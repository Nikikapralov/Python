text = input()
emoticons = []
for index_letter in range(len(text)):
    if text[index_letter] == ':':
        if not text[index_letter + 1].isdigit():
            result = text[index_letter]
            result += text[index_letter + 1]
            print(result)
