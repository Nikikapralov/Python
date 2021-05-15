from Send_data_to_client_in_real_time.Interface_Finder.Interface_finder_search_func import get_interfaces

""" The interface finder is to be used by the employees of Arivo. 
When a client has a request for a specific data point (key),
it could be quite daunting to find from which interface this data point can be derived from.
This is where the interface finder comes in! Simply enter the data point (key) into the search function,
which will then sweep all interfaces and return information about all interfaces containing such data points.
If you enter a key from an interface which has not been integrated, you will receive a "not_found" key
with list as value containing all the keys that were not found due to the interface not having been created yet
or a spelling mistake.
"""

list_of_keys = ['id', 'vehicle_id', 'gate', 'nothing']
print(get_interfaces(list_of_keys))
