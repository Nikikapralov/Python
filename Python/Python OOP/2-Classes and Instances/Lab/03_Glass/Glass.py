class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def enough_space(self, ml):
        if self.content + ml <= Glass.capacity:
            return True
        return False

    def fill(self, ml):
        if not self.enough_space(ml):
            return f'Cannot add {ml} ml'
        else:
            self.content += ml
            return f'Glass filled with {ml} ml'

    def empty(self):
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        space_left = Glass.capacity - self.content
        return f'{space_left} ml left'


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())


