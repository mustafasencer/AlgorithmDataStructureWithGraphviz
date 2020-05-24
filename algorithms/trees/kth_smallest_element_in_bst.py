"""
    Created by Mustafa Sencer Özcan on 24.05.2020.
"""
from data_structures.binary_search_tree.build.from_array import build_bst
from data_structures.tree.node import Node
from drawer.tree import TreeDrawer


class Solution:
    def kthSmallest(self, root: Node, k: int) -> int:
        stack = []
        while root or stack:
            while root and root.val is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return 0

    def recursive(self, root: Node, k: int):
        pass

    def recur_helper(self, root):
        pass


if __name__ == '__main__':
    array = [41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, None, 43, 46, 49, 0, 2, 30, 36, None, None, None, None, None,
             None, 45, 47, None, None, None, None, None, 4, 29, 32, None, None, None, None, None, None, 3, 9, 26, None,
             31, 34, None, None, 7, 11, 25, 27, None, None, 33, None, 6, 8, 10, 16, None, None, None, 28, None, None, 5,
             None, None, None, None, None, 15, 19, None, None, None, None, 12, None, 18, 20, None, 13, 17, None, None,
             22, None, 14, None, None, 21, 23]
    root = build_bst(array)
    TreeDrawer().visualize(root)
    result = Solution().kthSmallest(root, 25)
    print(result)
