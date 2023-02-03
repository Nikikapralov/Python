from DoublyLinkedLists.CircularDoublyLinkedList import CircularDoublyLinkedList

from Exercises.utils import generate_linked_list

linked_list = generate_linked_list(start=0, end=10, total=1000, linked_list_class=CircularDoublyLinkedList)
print(linked_list)

def remove_duplicates(linked_list):
    """
    Removes the duplicates from the linked list. Loop through list and add each unique value to a set. If value is in set,
    remove the value from the linked list.
    :param linked_list: The linked list.
    :return: Returns the linked list without duplicates.
    """
    set_of_values = set()
    counter = 1
    node = linked_list.head
    while True:
        if node.value not in set_of_values:
            set_of_values.add(node.value)
            counter += 1
            node = node.next
            continue
        node = node.next
        linked_list.pop(counter)
        if node == linked_list.head:
            break
    return linked_list

result = remove_duplicates(linked_list)
print(result)
