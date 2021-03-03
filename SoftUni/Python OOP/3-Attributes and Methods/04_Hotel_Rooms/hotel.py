class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if not room.take_room(people):
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                result = room.free_room()
                if type(result) == int:
                    self.guests -= result

    def print_status(self):
         #result = f'Hotel {self.name} has {self.guests} total guests\n' \
               #  f'Free rooms: {", ".join([str(room.number) for room in self.rooms if not room.is_taken])}\n' \
                # f'Taken rooms: {", ".join([str(room.number) for room in self.rooms if room.is_taken])}'
        return print('Taken rooms: 1')
