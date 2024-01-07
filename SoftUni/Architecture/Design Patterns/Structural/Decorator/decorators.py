from abc import ABC, abstractmethod


class AbstractDataHandler(ABC):
    """
    Defines an abstract component and its interfaces.
    """

    @abstractmethod
    def handle(self):
        pass


"""
Decorators must have the same interface as the thing they are decorating! They extend the functionality!
"""


class AbstractDataDecorator(AbstractDataHandler):
    """
    Defines an abstract decorator and its interfaces.
    """
    def __init__(self, handler):
        self.handler = handler

    def handle(self):
        pass


class EncryptionDecorator(AbstractDataDecorator):

    def handle(self):
        data = self.handler.handle()
        data.append("Encrypted")
        print("Returning my data from EncryptionDecorator after encryption.")
        return data


class CompressionDecorator(AbstractDataDecorator):

    def handle(self):
        data = self.handler.handle()
        data.append("Compressed")
        print("Returning my data from CompressionDecorator after compression.")
        return data


class DataHandler(AbstractDataHandler):

    def handle(self):
        data = ["My data"]
        print("Returning my data from DataHandler")
        return data

