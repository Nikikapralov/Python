class Vowels:
    VOWELS = 'aeiuo'

    def __init__(self, string):
        self.string = string
        self.index = -1

    def check_if_vowel(self, letter):
        return letter.lower() in self.VOWELS

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.index += 1
            if self.index == len(self.string):
                raise StopIteration
            letter = self.string[self.index]
            if self.check_if_vowel(letter):
                return letter

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
