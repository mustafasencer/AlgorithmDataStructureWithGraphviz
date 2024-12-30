from problems.tree.builds.build_bst_from_array import build_bst
from visualization.tree import TreeDrawer


def search_key(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search_key(root.right, key)

    return search_key(root.left, key)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 2, 4]
    root = build_bst(array)
    node = search_key(root, 4)
    TreeDrawer().visualize(node)
