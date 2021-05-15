"""All the required functionality summed in a simple function."""


def handle(controller, line):
    interface_str = controller.get_str_interface(line)
    list_values_interface = controller.get_list_values_and_interface_if_message_correct_type(interface_str)
    if not list_values_interface:
        return
    list_values, interface = list_values_interface
    data = controller.get_json_dictionary(line)
    result = controller.get_data(list_values, interface.create(data))
    """Maybe check the data (result) and modify it before sending? Sometimes, a piece of information may be missing,
    or the license plate may not make any sense at all. Is it reasonable to flood the client with such data? As per
    the task, if a license plate has not been detected, the information is not sent, although something can be detected
    going in and later going out."""
    try:
        if not result['id']:
            return
    except KeyError:
        pass
    result_json_object = controller.create_json_object(result)
    controller.post_data(result_json_object)
