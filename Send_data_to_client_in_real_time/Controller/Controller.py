from Send_data_to_client_in_real_time.Search_algorithm.Dict_search import find_value
from Send_data_to_client_in_real_time.Clients.Client import Client
from json import loads, dumps
from requests import post
from requests.exceptions import MissingSchema


"""Used to communicate between the Client and Interface classes."""


class Controller:
    def __init__(self, client: Client):
        self.client = client

    def get_data(self, list_values, interface_obj):
        result = {}
        for value in list_values:
            dictionary = self.__get_single_data_point(value, interface_obj)
            result.update(dictionary)
        return result

    @staticmethod
    def __get_single_data_point(data_point, interface_obj):
        result = {}
        if data_point in interface_obj.functions:
            result[data_point] = interface_obj.functions[data_point]
            if result[data_point] is not None:
                return result
        value = find_value(data_point, interface_obj.json_data)
        if isinstance(value, list) and len(value) == 1:
            value = value[0]
        result[data_point] = value
        return result

    @staticmethod
    def get_str_interface(line):
        index_cut = line.find(',')
        interface = line[2:index_cut - 1]
        return interface

    @staticmethod
    def get_json_dictionary(line):
        stop = len(line) - 2
        index_cut = line.find("{")
        json_dict = line[index_cut:stop]
        return loads(json_dict)

    @staticmethod
    def create_json_object(data):
        return dumps(data)

    """If the address is incorrect, this method will print the data for illustrative purposes of the task.
    In reality, it would throw an error with some message explaining what went wrong."""

    def post_data(self, data):
        try:
            post(self.client.server_address, data)
        except MissingSchema:
           print(data)

    """Checks if the message type is the correct one as per request of the client."""
    def get_list_values_and_interface_if_message_correct_type(self, interface_str):
        for interface, list_values in self.client.interface_data.items():
            if interface_str == str(interface):
                return list_values, interface
        return None



