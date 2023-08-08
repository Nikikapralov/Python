from abc import ABC, abstractmethod


class AbstractForm(ABC):

    @abstractmethod
    def fill_data(self):
        pass


class WindowsForm(AbstractForm):

    def fill_data(self):
        return "Windows data."


class MacOSForm(AbstractForm):

    def fill_data(self):
        return "MacOS data."
