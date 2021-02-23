string = input()
digits = ''
letters = ''
others = ''
for smth in string:
    if smth.isdigit():
        digits += smth
    elif smth.isalpha():
        letters += smth
    else:
        others += smth
print(digits)
print(letters)
print(others)