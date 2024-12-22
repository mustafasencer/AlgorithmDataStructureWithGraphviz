from problems.tree.tree_build_level_order import build_tree
from visualization.tree import TreeDrawer


def recursive(root):
    result = []

    def helper(root) -> None:
        if root:
            result.append(root.val)
            helper(root.left)
            helper(root.right)

    helper(root)
    return result


def stack(root):
    result = []
    stack = []
    current = root
    if not root:
        return None

    while current or stack:
        if current:
            stack.append(current)
            result.append(current.val)
            current = current.left
            continue
        node = stack.pop()
        current = node.right
    return result


def stack_1(root):
    if not root or not root.val:
        return []
    stack = []
    result = []
    while stack or root:
        while root:
            stack.append(root)
            result.append(root.val)
            root = root.left
        root = stack.pop()
        root = root.right
    return result


def stack_2(root):
    if not root:
        return []

    current = root
    stack = []
    result = []

    while stack or current:
        if current:
            stack.append(current)
            result.append(current.val)
            current = current.left
        else:
            current = stack.pop()
            current = current.right
    return result


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = build_tree(array, None, 0, len(array))
    result = stack(root)
    result_ = stack_1(root)
    result__ = stack_2(root)
    assert result_ == result
    TreeDrawer().visualize(root)
