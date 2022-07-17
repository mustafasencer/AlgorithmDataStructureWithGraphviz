from data_structures.tree import TreeNode
from problems.tree.tree_build_level_order import build_tree


def solution(root):
    def max_end(root):
        nonlocal max_value
        if not root:
            return 0
        left = max_end(root.left)
        right = max_end(root.right)
        max_value = max(max_value, left + root.val + right)
        return max(root.val + max(left, right), 0)

    max_value = 0
    max_end(root)
    return max_value


def solution_1(root: TreeNode) -> int:
    result = 0

    def dfs(root):
        nonlocal result
        if root is None or root.val is None:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        result = max(result, root.val + left + right)
        return max(root.val + max(left, right), 0)

    dfs(root)
    return result


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(array, None, 0, len(array))
    result = solution(root)
    result_ = solution_1(root)
    assert result_ == result
