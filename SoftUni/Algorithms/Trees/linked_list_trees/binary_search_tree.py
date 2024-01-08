from binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    """
    A tree made specifically for fast O(logN) searches.
    The right child is always higher than the root whereas the left child is always lower.
    """
    TRAVERSAL_FUNCTIONS = {"pre_order": BinaryTree._pre_order,
                           "in_order": BinaryTree._in_order,
                           "post_order": BinaryTree._post_order,
                           "level_order": BinaryTree._level_order}

    MAX_CHILDREN = 2

    def __init__(self, root_value=None, parent=None, duplicates=1):
        super().__init__(root_value=root_value, parent=parent)
        self.duplicates = duplicates

    def insert(self, value, node=None):
        """
        If value is None, first Node added, return self,
        if value is equal to node.value, duplicate +1, return
        if value is smaller go left,
        if value is bigger go right,
        before you branch, if next entry is None, add the Node at next entry.
        """
        if node is None:
            node = self

        if node.value is None:
            node.value = value
            return self

        if node.value == value:
            node.duplicates += 1
            return self

        if value < node.value:
            if node.nodes[0] is None:
                node.nodes[0] = BinarySearchTree(root_value=value, parent=node)
            else:
                node.insert(node=node.nodes[0], value=value)

        if value > node.value:
            if node.nodes[1] is None:
                node.nodes[1] = BinarySearchTree(root_value=value, parent=node)
            else:
                node.insert(node=node.nodes[1], value=value)

        return self

    def insert_at(self, to_insert_at, value):
        raise NotImplementedError("Not currently implemented.")

    def search(self, value, root_node=None):
        """
        If found return,
        if smaller go left,
        if bigger go right,
        repeat until found.
        If next is None and still not found, it does not exist.
        """

        if root_node is None:
            root_node = self

        if value == root_node.value:
            return root_node

        if value < root_node.value:
            if root_node.nodes[0] is None:
                raise ValueError(f"Value {value} does not exist.")
            root_node = self.search(value, root_node=root_node.nodes[0])

        if value > root_node.value:
            if root_node.nodes[1] is None:
                raise ValueError(f"Value {value} does not exist.")
            root_node = self.search(value, root_node=root_node.nodes[1])

        return root_node

    def delete(self, value, root_node=None):
        """
        Three cases.
        1. Leaf node - just delete the node.
        2. Has 1 child - node swap position with child then delete child.
        3. Has 2 children - find successor, swap position, delete successor. (Successor is lowest node in right branch of
        root)
        """
        if root_node is None:
            root_node = self

        if root_node.value is None:
            print("Cannot delete from empty tree.")
            return None

        if root_node.value < value:
            root_node.nodes[0] = self.delete(value=value, root_node=root_node.nodes[0])

        elif root_node.value > value:
            root_node.nodes[1] = self.delete(value=value, root_node=root_node.nodes[1])

        else:
            pass
        
        return self


    def min_value(self, root_node=None):
        """
        Go all the way to the left to find the minimum value.
        """
        if root_node is None:
            root_node = self

        if root_node.nodes[0] is None:
            return root_node

        return self.min_value(root_node=root_node.nodes[0])

    def max_value(self, root_node=None):
        """
        Go all the way to the right to find the maximum value.
        """
        if root_node is None:
            root_node = self

        if root_node.nodes[1] is None:
            return root_node

        return self.max_value(root_node=root_node.nodes[1])

    def clear(self):
        self.value = None
        self.nodes = [None] * self.MAX_CHILDREN
        self.parent = None
        self.duplicates = 1
        return self

    def __repr__(self):
        return str(self.value) + " " + str(self.duplicates)

    def __find_successor(self):
        successor = self.min_value(root_node=self.nodes[1])
        return successor

    @staticmethod
    def __get_index_left_right(node_to_delete):
        return [index for index, entry in enumerate(node_to_delete.parent.nodes)
                                    if entry == node_to_delete][0]


search_tree = BinarySearchTree()
search_tree.insert(100)
search_tree.insert(60)
search_tree.insert(70)
search_tree.insert(70)
search_tree.insert(40)
search_tree.insert(50)
search_tree.insert(120)
search_tree.insert(130)
print(search_tree.min_value())
print(search_tree.max_value())
print(search_tree.search(120), search_tree.search(120).parent)
print(search_tree.traverse())
print(search_tree.traverse(function="level_order"))