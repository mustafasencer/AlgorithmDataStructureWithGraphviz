"""
    Created by Mustafa Sencer Özcan on 23.05.2020.
"""
from data_structures.tree.build.level_order import build_tree
from data_structures.tree.node import Node
from drawer.tree import TreeDrawer


class Solution:
    def isValidBST(self, root: Node) -> bool:
        if not root:
            return False

        pre = None
        stack = []
        while root or stack:
            while root and root.val:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # should use a condition here
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True

    def recursive_sol(self, root: Node):
        return self.recur_util(root, -100000, 100000)

    def recur_util(self, root, min, max):
        if not root:
            return True
        if root.val and (root.val > max or root.val < min):
            return False

        return self.recur_util(root.left, min, root.val) and self.recur_util(root.right, root.val, max)


if __name__ == '__main__':
    array = [5, 1, 4, None, None, 3, 6]
    root = build_tree(array, None, 0, len(array))
    TreeDrawer().visualize(root)
    result = Solution().isValidBST(root)
    result_test = Solution().recursive_sol(root)
    assert result == result_test
    print(result)
