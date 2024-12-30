"""
Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

from problems.tree.builds.build_tree_level_order import build_tree
from visualization.tree import TreeDrawer


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode):
    if not root:
        return

    solution(root.left)
    solution(root.right)
    root.right, root.left = root.left, root.right
    return root


if __name__ == "__main__":
    array = [4, 2, 7, 1, 3, 6, 9]
    root = build_tree(array, len(array))
    TreeDrawer().visualize(root)
    result = solution(root)
    TreeDrawer().visualize(result)
