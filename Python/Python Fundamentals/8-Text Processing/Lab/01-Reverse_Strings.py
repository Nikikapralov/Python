result = ''


class String:
    def __init__(self, info):
        self.string = info
        self.gnirts = ''

    def reversed_1(self):
        self.gnirts = self.string[::-1]
        return f'{self.string} = {self.gnirts}\n'


while True:
    command = input()
    if command == 'end':
        break
    else:
        string_1 = String(command)
        result += string_1.reversed_1()
print(result)


