from data_structures.tree import TreeNode
from problems.tree.builds.build_bst_from_array import build_bst
from visualization.tree import TreeDrawer


def insert_key(root, node):
    if root is None:
        root = node
    elif root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert_key(root.right, node)
    elif root.left is None:
        root.left = node
    else:
        insert_key(root.left, node)
    return root


def in_order(root) -> None:
    if root:
        in_order(root.left)
        in_order(root.right)


if __name__ == "__main__":
    array = [4, 1, 4, 6, 7, 2]
    root = build_bst(array)
    node = insert_key(root, TreeNode(2))
    TreeDrawer().visualize(node)
