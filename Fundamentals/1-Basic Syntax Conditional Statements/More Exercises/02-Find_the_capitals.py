data = input()
capital_letters = []
for index, letter in enumerate(data):
    if letter.isupper():
        capital_letters.append(index)
print(capital_letters)
