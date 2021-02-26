class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'
        else:
            return f'Band {self.name} already has {album.name} in their library.'

    def remove_album(self, album_name):
        for album_object in self.albums:
            if album_object.name == album_name:
                if album_object.published:
                    return f'Album has been published. It cannot be removed.'
                else:
                    self.albums.remove(album_object)
                    return f'Album {album_name} has been removed.'
        return f'Album {album_name} is not found.'

    def details(self):
        data_1 = f'Band {self.name}\n'
        data_2 = ''
        for album_object in self.albums:
            data_2 += f'{album_object.details()}\n'
        result = data_1 + data_2
        return result
