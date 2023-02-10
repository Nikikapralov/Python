from collections import deque

"""
The root node is the tree itself.
When you give the traversal function a root node, that is actually the self.
Check if value of self.value is None, then set the value of self.value to value.
Else, continue checking the nodes of self, then each nodes of each node.
"""

class Tree:
    """
    When traversing, we go deep enough for the last nodes child to be None. Then we add this node first.
    So with post order traversal, we will go all the way to the left, check that this node has no right children as
    well and then if true add it. If not, we will go down the right children path.
    By using Pre Order Traversal, we will first print the first node, then go all the way to the left, then go all the
    way to the right, finally going back to print the first node.
    """
    def _pre_order(self, root_node, nodes=None, arguments=None):
        """
        Root Node
        then from Left to Right
        First Child
        Second Child
        Third Child
        etc
        """
        if nodes is None:
            nodes = []

        if not root_node:
            return nodes

        nodes.append(root_node)

        for node in root_node.nodes:
            nodes = self._pre_order(root_node=node, nodes=nodes)

        return nodes

    def _post_order(self, root_node, nodes=None, arguments=None):
        """
        From Left to Right
        First Child
        Second Child
        Third Child
        etc
        then
        Root Node
        """
        if nodes is None:
            nodes = []

        if not root_node:
            return nodes

        for node in root_node.nodes:
            nodes = self._post_order(root_node=node, nodes=nodes)

        nodes.append(root_node)
        return nodes

    def _level(self, root_node, nodes=None, arguments=None):
        """
        Siblings by depth level.
                        Root Node 1
       Root Node 2 and                Root Node 3
Root Node 4 and Root Node 5    Root Node 6 and Root node 7
        """

        if nodes is None:
            nodes = []

        if not root_node:
            return nodes

        queue = deque()
        queue.append(root_node)
        while queue:
            root = queue.popleft()
            nodes.append(root)
            for node in root.nodes:
                if node:
                    queue.append(node)
        return nodes

    def _in_order(self, root_node, nodes=None, arguments=None):
        """
        Root Node depends on arguments[0]. If 0, Root Node will be marked right after first child.
        First from Left to Right
        First Child
        Root Node
        Second Child
        Third Child
        """
        if not arguments:
            arguments = [0]

        root_node_order = arguments[0]

        if nodes is None:
            nodes = []

        if not root_node:
            return nodes

        for index in range(len(root_node.nodes)):
            node = root_node.nodes[index]
            nodes = self._in_order(root_node=node, nodes=nodes)
            if index == root_node_order:
                nodes.append(root_node)
        return nodes

    TRAVERSAL_FUNCTIONS = {"pre_order": _pre_order,
                           "in_order": _in_order,
                           "post_order": _post_order,
                           "level": _level}

    # A tree can have a variable amount of max children
    MAX_CHILDREN = 2

    def __init__(self, root_value=None, parent=None):
        self.value = root_value
        self.nodes = [None] * self.MAX_CHILDREN
        self.parent = parent

    def traverse(self, function="level", root_node=None, arguments=None):
        if not root_node:
            root_node = self

        if root_node.value is None:
            return []

        result = self.TRAVERSAL_FUNCTIONS[function](self, root_node=root_node, arguments=arguments)
        return result

    def insert(self, value):
        root_node = self
        queue = deque()
        queue.append(root_node)
        while queue:
            root = queue.popleft()

            #insert first ever element
            if not root.value:
                self.value = value
                return self

            for index in range(len(root.nodes)):
                node = root.nodes[index]
                if node:
                    queue.append(node)
                else:
                    root.nodes[index] = Tree(value, parent=root)
                    return self
        return f"The value {value} does not exist in the tree."

    def insert_at(self, to_insert_at, value):
        node_to_insert_at = self.search(to_insert_at)
        node_to_insert_at.insert(value)

    def search(self, value, root_node=None):
        if not root_node:
            root_node = self

        if not root_node:
            return "The provided root node is None. The tree is empty."

        queue = deque()
        queue.append(root_node)
        while queue:
            root = queue.popleft()
            if root.value == value:
                return root
            for node in root.nodes:
                if node:
                    queue.append(node)
        return f"The value {value} does not exist in the tree."

    def clear(self):
        self.value = None
        self.nodes = [None] * self.MAX_CHILDREN
        self.parent = None
        return self

    def delete(self, node_to_delete):
        if self is None:
            return "The tree is empty, cannot delete from empty tree."

        deepest_node = self.traverse()[-1]
        to_delete = self.search(value=node_to_delete)
        to_delete.value = deepest_node.value

        #delete first element resulting in the deletion of the entire tree
        if to_delete.parent is None:
            self.clear()
            return

        for index in range(len(deepest_node.parent.nodes)):
            node = deepest_node.parent.nodes[index]
            if node == deepest_node:
                deepest_node.parent.nodes[index] = None
        return

    def __repr__(self) -> str:
        return str(self.value)





