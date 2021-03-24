from project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):

    def __repr__(self):
        return f'{self.username} of type {self.__class__.__name__} has level {self.level}'