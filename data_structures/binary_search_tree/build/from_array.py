from drawer.tree import TreeDrawer
from data_structures.tree.node import Node


def build_bst(array):
    if not array:
        return None
    array = [i for i in array if i]

    array.sort()

    # find middle
    mid = int((len(array)) / 2)

    # make the middle element the root
    root = Node(array[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = build_bst(array[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = build_bst(array[mid + 1:])
    return root


if __name__ == '__main__':
    array = [1, 3, 5, 4, 2, 6, 7]
    root = build_bst(array)
    TreeDrawer().visualize(root)
