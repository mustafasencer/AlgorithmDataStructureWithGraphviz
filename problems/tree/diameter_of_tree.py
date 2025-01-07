from typing import Optional

from data_structures.tree import TreeNode
from problems.tree.builds.build_tree_level_order import build_tree


def solution(root: TreeNode) -> int:
    diameter = 0

    def dfs(node: Optional[TreeNode]):
        nonlocal diameter
        if node is None:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(left + right, diameter)
        return 1 + max(left, right)

    dfs(root)
    return diameter


if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5], 5)
    result = solution(root)
    assert result == 3
