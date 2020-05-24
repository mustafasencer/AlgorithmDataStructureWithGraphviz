"""
    Created by Mustafa Sencer Özcan on 24.05.2020.
"""
from data_structures.tree.build.level_order import build_tree
from data_structures.tree.node import Node


class Solution:
    def maxPathSum(self, root: Node) -> int:
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root or not root.val:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.result = max(self.result, root.val + left + right)
        return max(left, right) + root.val


if __name__ == '__main__':
    array = [-10, 9, 20, None, None, 15, 7]
    root = build_tree(array, None, 0, len(array))
    result = Solution().maxPathSum(root)
    print(result)
