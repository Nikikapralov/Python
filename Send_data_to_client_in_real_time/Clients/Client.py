"""Client object used for easily creating different clients."""


class Client:
    def __init__(self, interface_data: dict, server_address=None):
        self.interface_data = interface_data
        self.server_address = server_address

    @property
    def interface_data(self):
        return self.__interface_data

    @interface_data.setter
    def interface_data(self, value):
        if not isinstance(value, dict):
            raise ValueError('Please enter the data in a dictionary format.')
        self.__interface_data = value
