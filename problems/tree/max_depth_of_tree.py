from data_structures.tree import TreeNode
from problems.tree.builds.build_tree_level_order import build_tree


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, None, 6]
    root = build_tree(array, None, 0, len(array))
    result = max_depth(root)
    assert result == 3
