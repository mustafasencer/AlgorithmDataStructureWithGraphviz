"""
    Created by Mustafa Sencer Özcan on 24.05.2020.
    :arg Hard
"""
from data_structures.tree import TreeNode
from problems.tree_build_level_order import build_tree


class Solution:
    result = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if root is None or root.val is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.result = max(self.result, root.val + left + right, root.val)
        return max(root.val + left + right, 0)

    def maxPathSum_(self, root):
        def maxend(node):
            if not node:
                return 0
            left = maxend(node.left)
            right = maxend(node.right)
            self.max = max(self.max, left + node.val + right)
            return max(node.val + max(left, right), 0)

        self.max = 0
        maxend(root)
        return self.max


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(array, None, 0, len(array))
    result = Solution().maxPathSum(root)
    result_ = Solution().maxPathSum_(root)
    print(result)
    print(result_)
