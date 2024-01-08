from Search_algorithm.Dict_search import find_value
from Interfaces.Presence import Presence
from Interfaces.Vehicle_Image import VehicleImage

"""Returns the interfaces where the given key can be found."""


def find_interfaces(key_to_find):
    _interfaces = [Presence(), VehicleImage()]
    result = []
    for interface in _interfaces:
        for interface_type in interface.RAW_DATA:
            if find_value(key_to_find, interface_type[0]):
                result.append({str(interface): interface.__class__.__name__})
    return result


"""Uses the find_interfaces function for every key in the given list."""


def get_interfaces(list_of_keys):
    result = {'not_found': []}
    for key_to_find in list_of_keys:
        interface = (find_interfaces(key_to_find))
        if not interface:
            result['not_found'].append(key_to_find)
            continue
        result[key_to_find] = interface
    if not result['not_found']:
        result.pop('not_found')
    return result
