from drawer.tree import TreeDrawer
from data_structures.tree.build.level_order import build_tree


def recursive(root):
    result = []

    def helper(root, result):
        if root:
            result.append(root.val)
            helper(root.left, result)
            helper(root.right, result)
        return result

    return helper(root, result)


def stack(root):
    result = []
    stack = []
    current = root
    if not root:
        return

    while current or stack:
        if current:
            stack.append(current)
            result.append(current.val)
            current = current.left
            continue
        node = stack.pop()
        current = node.right
    return result


def stack_(root):
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


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(array, None, 0, len(array))
    result = stack(root)
    result_ = stack_(root)
    assert result_ == result
    TreeDrawer().visualize(root)
