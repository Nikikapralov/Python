from abc import ABC, abstractmethod

from Abstract_Factory.buttons import MacOSButton, WindowsButton
from Abstract_Factory.colours import Red
from Abstract_Factory.forms import MacOSForm, WindowsForm


class AbstractFactory(ABC):

    @abstractmethod
    def build_button(self, colour=Red()):
        pass

    @abstractmethod
    def build_form(self):
        pass


class MacOSFactory(AbstractFactory):

    def build_form(self):
        return MacOSForm()

    def build_button(self, colour=Red()):
        return MacOSButton(colour)


class WindowsFactory(AbstractFactory):

    def build_form(self):
        return WindowsForm()

    def build_button(self, colour=Red()):
        return WindowsButton(colour)