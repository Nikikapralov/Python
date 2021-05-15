import unittest
from Send_data_to_client_in_real_time.Controller.Controller import Controller
from Send_data_to_client_in_real_time.Clients.Client import Client
from Send_data_to_client_in_real_time.Interfaces.Presence import Presence
from requests.exceptions import MissingSchema


class TestHandle(unittest.TestCase):
    def setUp(self):
        self.client = Client({Presence(): ['id', 'direction']})
        self.message = str(["presence", {"all_ids":{"lpr":[]},"gateway":{"direction":"in","gate":"gate1"},"last_update":1611315708.731096,"medium":{},"name":"enter-om_alpr_tracking_1","present-area-name":"gate1","source":"gate1","timestamp":1611315708.731312,"type":"enter","vehicle_id":1611315708731091136}])
        self.controller = Controller(self.client)

    def test_get_interface_str_returns_str_of_interface_from_message(self):
        self.assertEqual('presence', self.controller.get_str_interface(self.message))

    def test_get_interface_and_requested_from_client_values_if_message_is_correct_type(self):
        self.interface_str = 'presence'
        interface_list_values = self.controller.get_list_values_and_interface_if_message_correct_type(self.interface_str)
        values = interface_list_values[0]
        interface = interface_list_values[1]
        self.assertTrue(isinstance(interface, Presence))
        self.assertEqual(['id', 'direction'], values)

    def test_get_json_dictionary_from_data(self):
        with open('data.log') as file:
            for line in file:
                if self.controller.get_str_interface(line) == 'presence':
                    self.message = line
                    break
        self.assertTrue(isinstance(self.controller.get_json_dictionary(self.message), dict))

    def test_get_expected_result_from_the_message_as_per_request_of_the_client(self):
        with open('data.log') as file:
            for line in file:
                if self.controller.get_str_interface(line) == 'presence':
                    self.message = line
                    break
        dictionary = self.controller.get_json_dictionary(self.message)
        self.assertEqual({'id': [], 'direction': 'in'},
                         self.controller.get_data(['id', 'direction'], Presence().create(dictionary)))

    def test_successfully_creates_a_json_object_from_the_result(self):
        self.result = {'id': [], 'direction': 'in'}
        self.assertTrue(isinstance(self.controller.create_json_object(self.result), str))

    """This test will not go through, since for the implementation of the task, we capture Missing Schema and Print 
    the output on the console. Remove the try: except: block from Controller method post_data for the test to work."""
    def test_post_returns_an_error_when_client_has_no_address(self):
        self.data = 'some data'
        with self.assertRaises(MissingSchema):
            self.controller.post_data(self.data)



