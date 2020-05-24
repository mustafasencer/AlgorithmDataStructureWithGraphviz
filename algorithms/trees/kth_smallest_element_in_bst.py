"""
    Created by Mustafa Sencer Özcan on 24.05.2020.
"""
from data_structures.tree.node import Node


class Solution:
    def kthSmallest(self, root: Node, k: int) -> int:
        stack = []
        while root or stack:
            while root:
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
    result = Solution().kthSmallest()
    print(result)
