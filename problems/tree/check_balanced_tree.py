from problems.tree.builds.build_tree_level_order import build_tree


def is_balanced(root):
    def check(root):
        if not root:
            return 0
        left = check(root.left)
        right = check(root.right)
        if right == -1 or left == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, None, 6]
    root = build_tree(array, None, 0, len(array))
    result = is_balanced(root)
    assert result is None
