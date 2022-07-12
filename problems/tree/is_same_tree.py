"""
    Created by Mustafa Sencer Özcan on 24.05.2020.

    Check again in Leetcode
"""
from data_structures.tree import TreeNode
from graphviz.tree import TreeDrawer
from problems.tree_build_level_order import build_tree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.dfs(p) == self.dfs(q)

    def dfs(self, node):
        stack = []
        result = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result

    def bfs(self, node):
        pass


if __name__ == "__main__":
    array = [1, 1]
    array1 = [1, None, 1]
    root = build_tree(array, None, 0, len(array))
    root1 = build_tree(array1, None, 0, len(array1))
    TreeDrawer().visualize(root)
    TreeDrawer().visualize(root1)
    result = Solution().isSameTree(root, root1)
    print(result)
