from DoublyLinkedLists.CircularDoublyLinkedList import Node
from random import randint


def generate_linked_list(start: int, end: int, total: int, linked_list_class):
    """
    Creates and fills a linked list, then returns it.
    :param start: Start range of the random.
    :param end: End range of the random.
    :param total: Total amount of objects.
    :param linked_list_class: The class of the linked list.
    :return: Returns the linked list.
    """
    items = [randint(start, end) for i in range(total)]
    linked_list = linked_list_class()
    for entry in items:
        linked_list.append(Node(entry))
    return linked_list