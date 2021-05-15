from Send_data_to_client_in_real_time.Controller.Controller import Controller
from Send_data_to_client_in_real_time.Clients.Client import Client
from Send_data_to_client_in_real_time.Interfaces.Presence import Presence
from Send_data_to_client_in_real_time.Interfaces.Vehicle_Image import VehicleImage
from Send_data_to_client_in_real_time.Handle.Handle import handle
from time import time

"""Main functionality. 
Create a Client object which accepts a dictionary and the address.
The dictionary consists of the requested Interface object as key and information to extract as values in list.
(You can have a dictionary with multiple keys. A client can ask for information from multiple interfaces and you can
effortlessly capture them and post them from the same Client object.)
Create an object Controller which receives the already created client.
For every message in the message queue, invoke the function handle, by passing it the controller object and the message.

NB: If you don't know in which interface the key holding the information the client has requested is located,
use the Interface Finder!

P.S. For this exercise, the messages will be printed on the screen since no real address has been provided, though the
implementation for post is ready and can be found in Controller.
"""

start_time = time()

client_bob = Client({Presence(): ['id', 'direction']})
controller = Controller(client_bob)

with open('data.log', 'r') as file:
    for line in file:
        handle(controller, line)

end_time = time()
print(f'Execution time: {(end_time - start_time):.4f} seconds.')


"""Proof that it works with multiple interfaces."""

#client_bob = Client({Presence(): ['id', 'direction'], VehicleImage(): ['vehicle_id']}, 'Some address')
#controller = Controller(client_bob)


#with open('data.log', 'r') as file:
    #for line in file:
        #handle(controller, line)


