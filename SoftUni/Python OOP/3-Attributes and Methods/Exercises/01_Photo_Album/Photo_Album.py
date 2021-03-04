class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for x in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):
        for index in range(self.pages):
            if len(self.photos[index]) == 4:
                continue
            else:
                self.photos[index].append(label)
                slot = len(self.photos)
                return f'{label} photo added successfully on page {index + 1} slot {slot}'
        return f'No more free spots'

    def display(self):
        line = f"{'-' * 11}\n"
        result = line
        for page in range(self.pages):
            result += ' '.join(['[]' for slot in range(len(self.photos[page]))])
            result += '\n'
            result += line
        return result

