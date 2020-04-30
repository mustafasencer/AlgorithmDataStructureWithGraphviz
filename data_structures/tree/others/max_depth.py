from data_structures.tree.node import Node


def max_depth(root: Node) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == '__main__':
    pass
