from problems.tree.tree_build_level_order import build_tree


def recursion(root):
    result = []

    def helper(root):
        if root:
            helper(root.left)
            result.append(root.val)
            helper(root.right)

    helper(root)
    return result


def stack(root):
    current = root
    stack = []
    result = []

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.val)
            current = current.right
    return result


def stack_(root):
    if not root or not root.val:
        return
    stack = []
    result = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(array, None, 0, len(array))
    result = stack(root)
    result_ = recursion(root)
    assert result == result_
    print(result)
