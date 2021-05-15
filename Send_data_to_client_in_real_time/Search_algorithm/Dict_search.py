"""Finds a value from a key in a nested dictionary."""


def find_value(key_to_find, search_dict):
    keys_found = []

    for key, value in search_dict.items():
        if key == key_to_find:
            if value not in keys_found:
                keys_found.append(value)
        elif isinstance(value, dict):
            results = find_value(key_to_find, value)
            for result in results:
                if result not in keys_found:
                    keys_found.append(result)
        elif isinstance(value, (list, tuple)):
            for item in value:
                if isinstance(item, dict):
                    more_results = find_value(key_to_find, item)
                    for another_result in more_results:
                        if another_result not in keys_found:
                            keys_found.append(another_result)
    return keys_found

