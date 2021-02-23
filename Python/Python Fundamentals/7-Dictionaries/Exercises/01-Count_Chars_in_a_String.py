class String:
    def __init__(self, string):
        self.string = string
        self.char_dict = {}
        self.filling_the_dict()

    def filling_the_dict(self):
        for char_key in self.string:
            if char_key == " ":
                continue
            elif char_key in self.char_dict:
                self.char_dict[char_key] += 1
            else:
                self.char_dict[char_key] = 1
        print(self.print_output(self.char_dict))

    def print_output(self, dictionary):
        result = ''
        for key, value in dictionary.items():
            result += f'{key} -> {value}\n'
        return result


string_1 = String(input())
