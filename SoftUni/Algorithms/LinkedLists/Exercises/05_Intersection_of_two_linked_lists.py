from DoublyLinkedLists.DoublyLinkedList import DoublyLinkedList, Node
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)
j = Node(10)

first_list = DoublyLinkedList().append(a).append(b).append(c).append(e).append(f).append(g).append(h)
second_list = DoublyLinkedList().append(d).append(e).append(f).append(g).append(h)
print(first_list)
print(second_list)

def find_intersection(first_list: DoublyLinkedList, second_list: DoublyLinkedList) -> Node:
    """
    Find the intersection of two linked lists that are connected.
    First check which list is longer than the other and by how much. Move to pointer from the first node, to the
    position equal to the difference of the size of both lists. Then, once the pointers of both lists have the same amount
    of nodes in front of them, start looping and searching for the intersection.
    :param first_list: The first list.
    :param second_list: The second list.
    :return: The intersection node.
    """

    if first_list.tail != second_list.tail:
        raise ValueError("Lists are not intersecting!")

    length_of_first = first_list.total_items
    length_of_second = second_list.total_items
    bigger = first_list if length_of_first - length_of_second >= 0 else second_list
    smaller = first_list if length_of_first - length_of_second < 0 else second_list

    catch_up = abs(length_of_first - length_of_second)
    first_node = smaller.head
    second_node = bigger.head

    for _ in range(catch_up):
        second_node = second_node.next

    while True:
        if first_node == second_node:
            intersection_node = first_node
            break
        first_node = first_node.next
        second_node = second_node.next
    return intersection_node


print(find_intersection(first_list, second_list))




