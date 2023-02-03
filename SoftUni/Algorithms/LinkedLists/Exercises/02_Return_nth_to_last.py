from DoublyLinkedLists.CircularDoublyLinkedList import CircularDoublyLinkedList

from Exercises.utils import generate_linked_list

linked_list = generate_linked_list(start=0, end=10, total=10, linked_list_class=CircularDoublyLinkedList)
print(linked_list)

def return_nth_to_last(linked_list, nth) -> int:
    """
    Returns the nth to last element. Create the pointers and move the simultaneously.
    Once the second reaches the end, the first will point at the nth to last item if properly spaced apart.
    Indexing begins from 1 as per Linked List specs.
    :param linked_list: The linked list
    :param nth: The nth to last element to be returned.
    :return: Returns the value of the node.
    """
    last = linked_list.head
    to_be_returned = linked_list.head
    counter = 1
    while True:
        if counter >= nth:
            to_be_returned = to_be_returned.next
        counter += 1
        last = last.next
        if last.next == linked_list.head:
            break

    return to_be_returned

print(return_nth_to_last(linked_list=linked_list, nth=6))


