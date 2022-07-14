from data_structures.tree import TreeNode
from problems.tree.tree_build_level_order import build_tree


class Solution:
    result = float("-inf")

    def max_path_sum(self, root):
        def max_end(node):
            if not node:
                return 0
            left = max_end(node.left)
            right = max_end(node.right)
            self.max = max(self.max, left + node.val + right)
            return max(node.val + max(left, right), 0)

        self.max = 0
        max_end(root)
        return self.max

    def max_path_sum_1(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if root is None or root.val is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.result = max(self.result, root.val + left + right)
        return max(root.val + max(left, right), 0)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(array, None, 0, len(array))
    result = Solution().max_path_sum(root)
    result_ = Solution().max_path_sum_1(root)
    print(result)
    print(result_)
