from abc import ABC, abstractmethod


class ClientInterface(ABC):

    @abstractmethod
    def request(self):
        pass


class ClientA(ClientInterface):

    def request(self):
        return "Request from client A"