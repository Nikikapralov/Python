from Trees.linked_list_trees.tree import Tree


class BinaryTree(Tree):

    TRAVERSAL_FUNCTIONS = {"pre_order": Tree._pre_order,
                           "in_order": Tree._in_order,
                           "post_order": Tree._post_order,
                           "level_order": Tree._level_order}

    MAX_CHILDREN = 2

    def __init__(self, root_value=None, parent=None):
        super().__init__(root_value=root_value, parent=parent)





