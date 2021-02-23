class String:
    def __init__(self, data):
        self.string = data
        self.n = len(self.string)

    def repeat_string_n_times(self):
        return self.string * self.n


result = ''

list_strings = input().split()
for string in list_strings:
    string_object = String(string)
    result += string_object.repeat_string_n_times()
print(result)

