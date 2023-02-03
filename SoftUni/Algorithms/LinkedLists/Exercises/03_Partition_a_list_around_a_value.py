from DoublyLinkedLists.CircularDoublyLinkedList import CircularDoublyLinkedList, Node

from Exercises.utils import generate_linked_list

linked_list = generate_linked_list(start=0, end=10, total=10, linked_list_class=CircularDoublyLinkedList)
print(linked_list)

def partition_around(linked_list, value):
    """
    Loop through the linked list, check each node. If the node is smaller than the required value,
    remove the node from the linked list and add it to the left of a new one. If is higher, remove and add to the right.
    At the end clear the old linked list to free memory.

    :param linked_list: The linked list.
    :param value: The value to be partitioned around.
    :return: The partitioned linked list.
    """
    partitioned = CircularDoublyLinkedList()
    for node in linked_list:
        if node.value <= value:
            partitioned.append_left(Node(node.value))
        else:
            partitioned.append(Node(node.value))
    linked_list.clear()
    return partitioned

print(partition_around(linked_list=linked_list, value=2))
