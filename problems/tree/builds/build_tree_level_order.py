from typing import Optional

from data_structures.tree import TreeNode


def build_tree(array: list[int], n: int, root: Optional[TreeNode] = None, index: int = 0) -> TreeNode:
    if index >= n:
        return root

    new_node = TreeNode(array[index])
    root = new_node
    root.left = build_tree(array, n, root.left, 2 * index + 1)
    root.right = build_tree(array, n, root.right, 2 * index + 2)

    return root
