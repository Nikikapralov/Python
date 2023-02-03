from DoublyLinkedLists.CircularDoublyLinkedList import CircularDoublyLinkedList, Node

first_list = CircularDoublyLinkedList().append(Node(7)).append(Node(1)).append(Node(6))
second_list = CircularDoublyLinkedList().append(Node(5)).append(Node(9)).append(Node(2))


def sum_lists(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = CircularDoublyLinkedList()

    while True:
        result = carry
        result += n1.value
        result += n2.value
        ll.append(Node(int(result % 10)))
        carry = result / 10
        if n1.next == llA.head or n2.next == llB.head:
            break
        n2 = n2.next
        n1 = n1.next

    return ll



print(sum_lists(first_list, second_list))

