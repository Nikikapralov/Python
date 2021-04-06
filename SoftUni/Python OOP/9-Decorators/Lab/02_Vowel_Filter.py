VOWELS = 'aeiou'

def vowel_filter(function):

    def wrapper():
        letters = []
        for letter in function():
            if letter.lower() in VOWELS:
                letters.append(letter)
        return letters

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
