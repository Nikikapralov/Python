class BinaryTree:

    def _pre_order(self, nodes=None, index=1):
        if self.nodes[1] is None:
            return []

        if nodes is None:
            nodes = []

        if index > self.last_used_index:
            return nodes

        nodes.append(self.nodes[index])

        nodes = self._pre_order(nodes=nodes, index=2 * index)
        nodes = self._pre_order(nodes=nodes, index=2 * index + 1)

        return nodes

    def _in_order(self, nodes=None, index=1):
        if self.nodes[1] is None:
            return []

        if nodes is None:
            nodes = []

        if index > self.last_used_index:
            return nodes

        nodes = self._in_order(nodes=nodes, index=2 * index)
        nodes.append(self.nodes[index])
        nodes = self._in_order(nodes=nodes, index=2 * index + 1)
        return nodes

    def _post_order(self, nodes=None, index=1):

        if self.nodes[1] is None:
            return []

        if nodes is None:
            nodes = []

        if index > self.last_used_index:
            return nodes

        nodes = self._in_order(nodes=nodes, index=2 * index)
        nodes = self._in_order(nodes=nodes, index=2 * index + 1)
        nodes.append(self.nodes[index])

        return nodes

    def _level(self):
        result = [node for node in self.nodes if node is not None]
        return result

    TRAVERSAL_FUNCTIONS = {"pre_order": _pre_order,
                           "in_order": _in_order,
                           "post_order": _post_order,
                           "level": _level}

    MAX_SIZE = 1024

    def __init__(self):
        self.nodes = [None] * self.MAX_SIZE
        self.last_used_index = 0

    def insert(self, value):
        for index in range(2):
            self.last_used_index += 1
            self.nodes[self.last_used_index + index] = value
            return self

    def traverse(self, function="level"):
        if self.nodes[1] is None:
            return []

        result = self.TRAVERSAL_FUNCTIONS[function](self)
        return result

    def search(self, value, start_index=1):
        for index in range(start_index, self.last_used_index + 1):
            node = self.nodes[index]
            if node == value:
                return value, index
        raise ValueError(f"Value to search {value} does not exist in binary tree with start node at index {start_index}")

    def delete(self, value):
        node_to_delete, index = self.search(value)
        swap_node = self.nodes[self.last_used_index]
        self.nodes[index] = swap_node
        self.nodes[self.last_used_index] = None
        self.last_used_index -= 1
        return self

    def clear(self):
        self.nodes = [None] * self.MAX_SIZE
        self.last_used_index = 0

    def get_parent(self, node_index):
        parent_index = node_index // 2
        return self.nodes[parent_index]

    def __repr__(self):
        return str(self.value)


tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
print(tree.get_parent(6))
print(tree.traverse())
print(tree.traverse(function="pre_order"))
print(tree.traverse(function="in_order"))
print(tree.traverse(function="post_order"))




