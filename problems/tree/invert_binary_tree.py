"""
Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

from problems.tree.builds.build_tree_level_order import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode):
    if not root:
        return

    temp = root
    temp.left = root.right
    temp.right = root.left
    solution(root.left)
    solution(root.right)

    return temp


if __name__ == "__main__":
    array = [4, 2, 7, 1, 3, 6, 9]
    root = build_tree(array, None, 0, len(array))
    result = solution(root)
    assert result == [4, 7, 2, 9, 6, 3, 1]
