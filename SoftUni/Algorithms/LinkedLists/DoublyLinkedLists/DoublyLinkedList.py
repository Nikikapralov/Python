class Node:
    """
    Node of singly linked list. Has next property which links it to the next node and value property to hold the value.
    """

    node_identifier = 0

    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value
        self.identifier = self.node_identifier + 1
        Node.node_identifier += 1

    def __repr__(self):
        return str(self.value)


class DoublyLinkedList:
    """
    Doubly linked list implementation.
    The following implementation provides a multitude of methods for interaction with the DoublyLinkedList class.
    This implementation forbids the user from attempting to assign an already assigned Node into the list. For example,
    Node A has been assigned to position 3. We cannot reassign Node A to position 4 unless we remove it first. This has
    been made so in order to protect data integrity and make sure that each change of the Linked list is desired and not
    made by a programmer mistake.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.total_items = 0
        self.node_identifiers = []

    def append(self, node: Node):
        """
        Appends a node to the end of the linked list.
        :param node: A node holding a value and a link to the next node.
        :return: Return self.
        """
        self.__validate_is_node_instance(node)

        if self.__is_head_none():
            self.__set_first_node(node)
            self.__update_linked_list_properties(node, "add")
            return self

        self.__validate_identifier_node_unique_in_list(node.identifier)

        node.next = None
        node.previous = self.tail
        self.tail.next = node
        self.tail = node
        self.__update_linked_list_properties(node, "add")
        return self

    def append_left(self, node: Node):
        """
        Appends a new node at the start of the Linked List.
        :param node: A node holding a value and a link to the next node.
        :return: Returns self.
        """
        self.__validate_is_node_instance(node)

        if self.__is_head_none():
            self.__set_first_node(node)
            self.__update_linked_list_properties(node, "add")
            return self

        self.__validate_identifier_node_unique_in_list(node.identifier)

        node.next = self.head
        self.head.previous = node
        self.head = node
        self.__update_linked_list_properties(node, "add")
        return self

    def insert(self, node: Node, position: int):
        """

        :param node: A node holding a value and a link to the next node.
        :param position: The position at which the node is to be inserted. When position 2 in a Linked List with 5 items,
        the new 6th node will be inserted at position 2 and will become the second node, pushing the other 4 to the right.
        :return: Returns self.
        """
        self.__validate_is_node_instance(node)
        self.__validate_is_int_instance(position)
        self.__validate_position(position)
        self.__validate_identifier_node_unique_in_list(node.identifier)

        if position == 1:
            self.append_left(node)
            return self

        if position == self.total_items + 1:
            self.append(node)
            return self

        previous_node = self.__get_node(position - 1)
        next_node = previous_node.next
        next_node.previous = node
        previous_node.next = node
        node.previous = previous_node
        node.next = next_node
        self.__update_linked_list_properties(node, "add")
        return self

    def delete(self, entry) -> Node:
        """
        Deletes the node with the given value. Deletes the first found node with such a value. If not such node exists,
        raise an error.
        :param entry: Value of node which is to be deleted.
        :return: Returns the value itself.
        """

        previous_node = None
        for node in self:
            if node.value == entry:
                if not previous_node:
                    if node == self.head and node == self.tail:
                        self.head = None
                        self.tail = None
                        node.next = None
                        node.previous = None
                    else:
                        self.head = node.next
                        self.head.previous = None
                        node.next = None
                        node.previous = None

                elif node == self.tail:
                    self.tail = previous_node
                    self.tail.next = None
                    node.next = None
                    node.previous = None
                else:
                    previous_node.next = node.next
                    node.next.previous = previous_node
                    node.next = None
                    node.previous = None
                self.__update_linked_list_properties(node, "remove")
                return node.value
            previous_node = node

    def pop(self, position=None) -> Node:
        """
        Deletes the last node or the node at the given position.
        :param position: The position of the node which is to be deleted (Not necessary).
        :return: Returns the node itself.
        """
        if position:
            self.__validate_is_int_instance(position)
            if not (1 <= position <= self.total_items):
                raise ValueError(f"The current position does not exist in a Linked List with {self.total_items} items.\n"
                                 f"Available positions are 1 to {self.total_items}")
        if not position:
            position = self.total_items

        counter = 1
        previous_node = None
        for node in self:
            if counter == position:
                if not previous_node:
                    if node == self.head and node == self.tail:
                        self.head = None
                        self.tail = None
                        node.next = None
                        node.previous = None
                    else:
                        self.head = node.next
                        self.head.previous = None
                        node.next = None
                        node.previous = None

                elif position == self.total_items:
                    self.tail = previous_node
                    self.tail.next = None
                    node.next = None
                    node.previous = None

                else:
                    previous_node.next = node.next
                    node.next.previous = previous_node
                    node.next = None
                    node.previous = None

                self.__update_linked_list_properties(node, "remove")
                return node.value
            previous_node = node
            counter += 1

    def find(self, entry) -> Node:
        """
        Finds a node in the linked list with the value and return it.
         If multiple nodes have the same value return the first one. If no such node exists, raises an error.
        :param entry: A value of a node.
        :return: The found node or raises Error if no such Node has been found.
        """
        for node in self:
            if node.value == entry:
                return node.value
        raise ValueError(f"Value {entry} was not found in the linked list.")

    def find_position(self, entry) -> int:
        """
        Finds the position of the node with the desired value. If multiple nodes have the same value.
        Returns the first one found. If no such node exists, raises an error.
        :param node: Value entry of the node that is to be searched for.
        :return: Position of node as integer.
        """
        counter = 1
        for node in self:
            if node.value == entry:
                return counter
            counter += 1

        raise ValueError(f"No such value {entry} in the linked list.")

    def clear(self) -> None:
        """
        Clears the Linked List.
        Loop through all items to set the previous to null in order to be eligible for garbage collection.
        Sets Head and Tail to Null.
        :return: Returns None
        """

        for node in self:
            try:
                node.previous.next = None
            except AttributeError:
                pass

            node.previous = None

        self.head = None
        self.tail = None
        self.total_items = len([i for i in self])
        self.node_identifiers = []

    def __getitem__(self, position: int) -> Node:
        """
        Returns the position of the node in the given LinkedList
        :param position: Position of the wanted node in the LinkedList.
        :return: Return the Node.
        """
        self.__validate_is_int_instance(position)
        return self.__get_node(position)

    def __setitem__(self, position: int, node: Node) -> None:
        """
        Sets the value of the node at the current position. Removes the previous value.
        :param node: A node holding a value and a link to the next node.
        :param position: The position at which the node is to be inserted. When position 2 in a Linked List with 5 items,
        the new 6th node will be inserted at position 2 and will become the second node, pushing the other 4 to the right.
        :return: Returns None.
        """
        self.__validate_is_int_instance(position)
        self.__validate_is_node_instance(node)
        self.pop(position)
        self.insert(node, position)

    def __contains__(self, entry) -> bool:
        """
        Returns a bool answer if the LinkedList includes the Node.value (entry).
        :param entry: The value to be searched for among the nodes..
        :return: Boolean answer.
        """
        for node in self:
            if node.value == entry:
                return True
        return False

    def __iter__(self):
        """
        Allows to iterate the Linked List.
        :return: Returns None.
        """
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def reverse_iter(self):
        """
        Allots to iterate the Linked List in reverse.
        :return: Returns None.
        """
        current_node = self.tail
        while current_node is not None:
            yield current_node
            current_node = current_node.previous

    def __repr__(self) -> str:
        """
        Returns a list like representation of the linked list:
        :return: List like representation.
        """
        if self.total_items == 0:
            return "[]"
        representation = "["
        for node in self:
            representation += f"{node.value} <-> "
        representation = representation[:-4] + "]"
        return representation

    def __is_head_none(self) -> bool:
        """
        Check if the self.head attribute is none.
        :return: Boolean
        """
        return True if self.head is None else False

    def __set_first_node(self, node: Node) -> None:
        """
        Set the head and the tail to the first node in the linked list.
        :param node: The node.
        :return: Returns None.
        """
        self.head = node
        self.tail = node

    def __validate_position(self, position: int) -> None:
        """
        Validate that the position is in the required range for insertion.
        :param position: Position to be inserted at.
        :return: Returns None.
        """
        if not 1 <= position <= self.total_items + 1:
            raise ValueError(f"The given position {position} is out of range of Linked List with items: {self.total_items}.\n"
                             f"Possible range: 1 to {self.total_items + 1}")

    def __get_node(self, position_of_node: int):
        """
        Returns the node at the position.
        :param position_of_node: Integer.
        :return: Returns None.
        """
        counter = 1
        for current_node in self:
            if position_of_node == counter:
                return current_node
            counter += 1

    def __update_linked_list_properties(self, node: Node, action: str) -> None:
        """
        Updates the linked list properties. On removal, sets total items to - 1 and removes an identifier.
        :param node: Node.
        :param action: Action, remove or add. Some code smell, but im running out of time.
        :return:
        """
        if action == "add":
            self.total_items += 1
            self.node_identifiers.append(node.identifier)
        if action == "remove":
            self.total_items -= 1
            self.node_identifiers.remove(node.identifier)

    def __validate_identifier_node_unique_in_list(self, identifier: int) -> None:
        if identifier in self.node_identifiers:
            raise ValueError("Node already exists in the linked list. In order to move the node, first remove it and then add it.")

    @staticmethod
    def __validate_is_node_instance(node):
        if not isinstance(node, Node):
            raise TypeError(
                f"Provided value {node} is not of type Node. Please import class note and create the node instance\n"
                f"as follows: Node({node})")

    @staticmethod
    def __validate_is_int_instance(position):
        if not isinstance(position, int):
            raise TypeError(
                f"Provided value {position} is not of type integer. Please provide the position as an integer.")




