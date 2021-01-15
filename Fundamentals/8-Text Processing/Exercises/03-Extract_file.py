class File:
    def __init__(self, path):
        self.name = None
        self.extension = None
        self.path = path
        self.get_name_extension()

    def get_name_extension(self):
        list_of_path = self.path.split('\\')
        self.name, self.extension = list_of_path[-1].split('.')


file_1 = File(input())
print(f'File name: {file_1.name}')
print(f'File extension: {file_1.extension}')


