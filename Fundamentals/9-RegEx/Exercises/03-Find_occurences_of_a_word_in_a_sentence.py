import re
data = input()
word = input()
word_lowercase = word.lower()
data_lowercase = data.lower()
pattern = fr"\b{word_lowercase}\b"
result = re.findall(pattern, data_lowercase)
print(len(result))