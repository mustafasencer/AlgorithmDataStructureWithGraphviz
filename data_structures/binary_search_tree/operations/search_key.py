from data_structures.binary_search_tree.build.from_array import build_bst
from drawer.tree import TreeDrawer


def search_key(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search_key(root.right, key)

    return search_key(root.left, key)


def search_deneme(root, key):
    if not root:
        return None
    if root.val == key:
        return root

    if root.val > key:
        return search_deneme(root.left, key)
    return search_deneme(root.right, key)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 2, 4]
    root = build_bst(array)
    node = search_deneme(root, 4)
    TreeDrawer().visualize(node)
