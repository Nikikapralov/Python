class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song):
        if song not in self.songs:
            if song.single:
                return f"Cannot add {song.name}. It's a single"
            elif self.published:
                return f'Cannot add songs. Album is published.'
            else:
                self.songs.append(song)
                return f'Song {song.name} has been added to the album {self.name}.'
        elif song in self.songs:
            return f'Song is already in the album.'

    def remove_song(self, song_name):
        if self.published:
            return f'Cannot remove songs. Album is published.'
        for song_object in self.songs:
            if song_object.name == song_name:
                self.songs.remove(song_object)
                return f'Removed song {song_name} from album {self.name}.'
        return f'Cannot remove songs. Album is published.'

    def publish(self):
        if not self.published:
            self.published = True
            return f'Album {self.name} has been published.'
        else:
            return f'Album {self.name} is already published.'

    def details(self):
        data_1 = f'Album {self.name}\n'
        data_2 = ''
        for song in self.songs:
            data_2 += f'== {song.get_info()}\n'
        result = data_1 + data_2
        return result
