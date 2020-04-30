from drawer.tree import TreeDrawer
from data_structures.tree.node import Node


def insert(root, node):
    if root is None:
        return node
    if root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
    return root


def build_bst(array):
    root = None
    for elem in array:
        node = Node(elem)
        root = insert(root, node)
    return root


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    root = build_bst(array)
    TreeDrawer().visualize(root)
