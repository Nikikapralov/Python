with open(r'roman.txt', 'r') as data:
    all_letters = {}
    for index in range(1, 1001):
        text = data.readline()
        number, letter = text.split(': ')
        all_letters[letter[:-1]] = int(number)
    text = data.readline()
    all_letters[letter] = int(number)
    all_letters.pop('')

roman = all_letters
